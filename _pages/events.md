---
layout: page
title: Events
permalink: /events/
---

<style>
  .date-label {
    display: inline-block;
    padding: 2px 8px;
    margin-right: 8px;
    background-color: #f0f0f0;
    border-radius: 12px;
    font-size: 0.8em;
  }
  .center-cell {
    text-align: center; /* Center align text horizontally */
    vertical-align: middle; /* Center align text vertically */
  }
  .today-event {
    background-color: #e6f3ff;
    border-left: 4px solid #0066cc;
    padding: 10px;
    margin: 5px 0;
  }
  .today-label {
    display: inline-block;
    padding: 2px 8px;
    margin-right: 8px;
    background-color: #0066cc;
    color: white;
    border-radius: 12px;
    font-size: 0.8em;
    font-weight: bold;
  }
  .host-label {
    display: inline-block;
    padding: 2px 8px;
    margin-right: 8px;
    background-color: #f0f0f0;
    border-radius: 12px;
    font-size: 0.8em;
  }
</style>

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
            <span class="today-label">TODAY</span>
          {% else %}
            <span class="date-label">{{ event.date }}</span>
          {% endif %}
          {% if event.host != nil and event.host != "" %}
            <span class="host-label">hosted by {{ event.host }}</span>
          {% endif %}
          <br>
          <strong><a href="{{ event.event_link }}">{{ event.edition }}</a></strong>
        </td>
      </tr>
    {% endif %}
  {% endfor %}
</table>
{% endif %}


### Statistics of past events

<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Edition</th>
      <th>Registrations</th>
      <th>Participants</th>
      <th>Recordings</th>
    </tr>
  </thead>
  <tbody>
    {% for event in site.data.events %}
      
    {% assign event_date = event.date | date: "%Y-%m-%d" %}
    {% assign today = site.time | date: "%Y-%m-%d" %}
  
    {% if event_date < today %}

    <tr>
      <td>{{ event.id }}</td>
      <td>
        <span class="date-label">{{ event.date }}</span><br>
        <a href="{{ event.event_link }}">{{ event.edition }}</a>
      </td>
      <td class="center-cell">{{ event.registrations }}</td>
      <td class="center-cell">{{ event.participants }}</td>
      <td>
        {% if event.recording.size == 0 %}
          In person only
        {% else %}
          {% for recording in event.recording %}
            {% if recording.link %}
              <a href="{{ recording.link }}">{{ recording.title }}</a><br>
            {% else %}
              {{ recording.title }}<br>
            {% endif %}
            {% if forloop.last == false %}
              <br>
            {% endif %}
          {% endfor %}
        {% endif %}
      </td>
    </tr>
    {% endif %}
    {% endfor %}
  </tbody>
</table>
