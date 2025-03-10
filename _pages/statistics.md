---
layout: page
title: Statistics
permalink: /statistics/
---

### Statistics

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
</style>

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
    {% endfor %}
  </tbody>
</table>
