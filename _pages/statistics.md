---
layout: page
title: Statistics
permalink: /statistics/
---

### Statistics

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
      <td><a href="{{ event.event_link }}">{{ event.edition }}</a></td>
      <td>{{ event.registrations }}</td>
      <td>{{ event.participants }}</td>
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
