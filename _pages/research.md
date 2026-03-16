---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
header:
  og_image: "research/ecdf.png"
---

My research interests primarily lie within two areas: 1) leveraging bottom-up approaches to develop quantum materials and methods to study them, and 2) understanding underlying physics of spin, charge, and light in such materials to harness them in a fast, efficient, scalable manner. 

I am interested in the following materials in no particular order: Diamond, SiC, hBN, TMDs, Graphene, AlN/GaN, SiO2, SiN

Here is some research I have recently been involved in beginning with most recent to less recent. While I have endeavored to gain expertise across diverse material systems, my interests now are more focused within semiconducting/dielectric/superconducting materials.

<!-- <div style="margin-top: 50px;"></div> -->

{% include base_path %}

{% assign ordered_pages = site.research | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %}

<div style="clear: both;"></div>

<!--- 
<html>
   <head>
      <title>HTML Video embed</title>
   </head>
   <body>
      <p>Self-assembly of a coarse-grained lipid chain modelled on the magic-sized cluster</p>
      <br />
      <iframe width="480" height="350" src="../assets/video/self-assembly.mp4" frameborder="0" allowfullscreen></iframe>
      </iframe>
   </body>
</html>
-->
