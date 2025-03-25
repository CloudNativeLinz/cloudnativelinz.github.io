---
layout: page
title: Meetups
permalink: /meetups/
---

{% for event in site.data.events %}

* [{{event.edition}}]({{ event.edition | datapage_url: 'meetup' | remove: '.html' }})

{% endfor %}