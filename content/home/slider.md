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
      content: World-Class AI & Medical Image Analysis Lab from HKUST
      align: center
      background:
        position: right
        color: '#666'
        brightness: 0.7
        media: hkust.jpg
    - title:  Human-centered Medical Image Analysis AI for Healthcare
      content: AI in Breast Cancer
      align: left
      background:
        position: center
        color: '#555'
        brightness: 0.7
        media: contact.jpg
    - title: Trustworthy AI for healthcare
      content: AI in pathology
      align: right
      background:
        position: center
        color: '#333'
        brightness: 0.5
        media: wsi.png
      link:
        icon: graduation-cap
        icon_pack: fas
        text: Join Us
        url: ../contact/
---
