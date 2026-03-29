/**
 * Topic pages: highlight TOC link for the section in view while scrolling.
 * Expects kramdown auto_ids on h2/h3 and toc-learning links href="#id".
 */
(function () {
  'use strict';

  function init() {
    var article = document.querySelector('.topic-article .page__content');
    var menu = document.querySelector('.topic-sidebar .toc__menu');
    if (!article || !menu) return;

    var headings = article.querySelectorAll('h2[id], h3[id]');
    var links = menu.querySelectorAll('a[href^="#"]');
    if (!headings.length || !links.length) return;

    var byId = {};
    links.forEach(function (a) {
      var href = a.getAttribute('href');
      if (href && href.length > 1) {
        byId[href.slice(1)] = a;
      }
    });

    var offset = 120;

    function updateActive() {
      var scrollLine = window.scrollY + offset;
      var activeId = headings[0].id;
      for (var i = 0; i < headings.length; i++) {
        var h = headings[i];
        var top = h.getBoundingClientRect().top + window.scrollY;
        if (top <= scrollLine) {
          activeId = h.id;
        }
      }
      links.forEach(function (a) {
        a.classList.remove('active');
      });
      if (activeId && byId[activeId]) {
        byId[activeId].classList.add('active');
      }
    }

    var ticking = false;
    function onScroll() {
      if (!ticking) {
        window.requestAnimationFrame(function () {
          updateActive();
          ticking = false;
        });
        ticking = true;
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    updateActive();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
