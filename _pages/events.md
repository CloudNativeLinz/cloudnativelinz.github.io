---
layout: page
title: Events
permalink: events/
---

{% assign upcoming_events = false %}
{% for event in site.data.events %}
  {% assign event_date = event.date | date: "%Y-%m-%d" %}
  {% assign today = site.time | date: "%Y-%m-%d" %}
  {% if event_date >= today %}
    {% assign upcoming_events = true %}
    {% break %}
  {% endif %}
{% endfor %}

{% if upcoming_events %}
### Upcoming events
<table width="100%" style="border: 5px solid #ccc; border-collapse: collapse;">
  {% for event in site.data.events %}
    {% assign event_date = event.date | date: "%Y-%m-%d" %}
    {% assign today = site.time | date: "%Y-%m-%d" %}
    {% if event_date >= today %}
      <tr {% if event_date == today %}class="today-event"{% endif %}>
        <td>
          {% if event_date == today %}
            <span class="label">TODAY</span>
          {% else %}
            <span class="label">{{ event.date }}</span>
          {% endif %}
          {% if event.host != nil and event.host != "" %}
            <span class="label">hosted by {{ event.host }}</span>
          {% endif %}
          <br>
        {% if event.event_link != nil and event.event_link != "" %}
            <strong><a href="{{ event.title | datapage_url: 'meetup' | remove: '.html' }}">{{ event.title }}</a></strong>
          {% else %}
            <strong>{{ event.title }}</strong>
          {% endif %}

        </td>
      </tr>
    {% endif %}
  {% endfor %}
</table>
{% endif %}


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