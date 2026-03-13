const AV_KEY = 'YOUR_API_KEY_HERE';
let tickerChartInst = null;
async function fetchTicker() {
  const ticker = document.getElementById('tickerInput').value.trim().toUpperCase();
  const status = document.getElementById('tickerStatus');
  if (!ticker) return;
  status.textContent = `Loading ${ticker}...`;
  try {
    const url = `https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=${ticker}&outputsize=compact&apikey=${AV_KEY}`;
    const res  = await fetch(url);
    const json = await res.json();
    const series = json['Time Series (Daily)'];
    if (!series) {
      status.textContent = json['Note'] || json['Information'] || `No data for "${ticker}"`;
      return;
    }
    const entries = Object.entries(series).slice(0, 30).reverse();
    const dates  = entries.map(([d]) => d.slice(5));
    const prices = entries.map(([, v]) => +parseFloat(v['4. close']).toFixed(2));
    const color  = prices[prices.length-1] >= prices[0] ? '#16a34a' : '#dc2626';
    if (tickerChartInst) tickerChartInst.destroy();
    tickerChartInst = new Chart(document.getElementById('tickerChart'), {
      type: 'line',
      data: {
        labels: dates,
        datasets: [{
          label: ticker,
          data: prices,
          borderColor: color,
          borderWidth: 2,
          pointRadius: 2,
          tension: 0.3,
          fill: true,
          backgroundColor: color + '22'
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: 'top' },
          title: { display: true, text: `${ticker} — Last 30 Trading Days` }
        },
        scales: { y: { ticks: { callback: v => '$' + v } } }
      }
    });
    status.textContent = '';
  } catch(e) {
    status.textContent = 'Fetch failed: ' + e.message;
  }
}
document.addEventListener('DOMContentLoaded', fetchTicker);