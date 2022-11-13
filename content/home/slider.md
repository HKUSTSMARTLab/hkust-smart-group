---
widget: slider
weight: 1
active: true
headless: true

design:
  # Slide height is automatic unless you force a specific height (e.g. '400px')
  slide_height: ''
  is_fullscreen: true
  # Automatically transition through slides?
  loop: false
  # Duration of transition between slides (in ms)
  interval: 2000

content:
  slides:
    - title: Welcome to SMART Lab
      # content: World-Class AI & Medical Image Analysis Lab from HKUST
      align: up
      background:
        position: right
        color: '#666'
        brightness: 0.7
        media: hkust.png
      link:
        icon: graduation-cap
        icon_pack: fas
        text: Join Us
        url: ../contact/
    - title: Trustworthy AI for Healthcare
      content: AI in Computational Pathology
      align: right
      background:
        position: center
        color: '#333'
        brightness: 0.5
        media: wsi.jpg
    - title:  Patient-centered Medical Imaging and Analysis
      content: AI in Multimodal Breast Cancer Analysis
      align: left
      background:
        position: center
        color: '#555'
        brightness: 0.7
        media: mri.png
---
