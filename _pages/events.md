---
layout: page
title: Events
permalink: events/
---

{% include upcoming-events.html %}

## Past Events

<table width="100%" style="border: 5px solid #ccc; border-collapse: collapse;">
{% for event in site.data.events reversed %}

 {% assign event_date = event.date | date: "%Y-%m-%d" %}
 {% assign today = site.time | date: "%Y-%m-%d" %}
  
 {% if event_date < today %}


  <tr>
        <td>
          {% if event_date == today %}
            <span class="today-label">TODAY</span>
          {% else %}
            <span class="label">{{ event.date }}</span>
          {% endif %}
          {% if event.host != nil and event.host != "" %}
            <span class="label">hosted by {{ event.host }}</span>
          {% endif %}
          <br>
          <strong><a href="{{ event.title | datapage_url: 'meetup' | remove: '.html' }}">{{ event.title }}</a></strong>
        </td>
      </tr>


    {% endif %}

{% endfor %}
</table>