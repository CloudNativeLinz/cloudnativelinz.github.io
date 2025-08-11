---
layout: page
title: 📊 Community Statistics
permalink: /statistics/
---

<div class="stats-intro">
  <p class="lead">Discover insights about our Cloud Native Computing Linz community. Explore event timelines, hosting organizations, speaker contributions, and participation trends that showcase our growing ecosystem.</p>
</div>

<div id="charts-status" class="alert-info" style="display: none;">
  <strong>📊 Loading interactive charts...</strong> If charts don't appear, static data tables will be shown instead.
</div>

<div id="fallback-notice" class="alert-warning" style="display: none;">
  <strong>📋 Interactive charts unavailable:</strong> Displaying data in table format. Charts require external resources that may be blocked by network restrictions.
</div>

<div class="stats-grid">
  <div class="stat-section">
    <h3>🏢 Top 15 Host Organizations</h3>
    <div class="chart-container">
      <canvas id="hostOrganizationsChart"></canvas>
      <div id="hostOrganizationsFallback" style="display: none;">
        <div class="chart-title">📊 Host Organizations</div>
        <table class="stats-table">
          <thead>
            <tr>
              <th>Host Organization</th>
              <th>Events Hosted</th>
              <th>Visual Representation</th>
            </tr>
          </thead>
          <tbody>
            {% comment %} Host organizations ordered by event count, then by most recent hosting date {% endcomment %}
            {% comment %} 3 events hosted (most recent first) {% endcomment %}
            <tr><td>Gepardec</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 30px;"></span> 3</td></tr>
            <tr><td>Cloudflight</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 30px;"></span> 3</td></tr>
            <tr><td>Dynatrace</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 30px;"></span> 3</td></tr>
            {% comment %} 2 events hosted (most recent first) {% endcomment %}
            <tr><td>netcetera</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 20px;"></span> 2</td></tr>
            <tr><td>karriere.at</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 20px;"></span> 2</td></tr>
            <tr><td>Public Cloud Group</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 20px;"></span> 2</td></tr>
            <tr><td>Runtastic</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 20px;"></span> 2</td></tr>
            {% comment %} 1 event hosted (most recent first) {% endcomment %}
            <tr><td>MIC</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
            <tr><td>tractive</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
            <tr><td>cloudxcelerate</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
            <tr><td>eww IT and TEL</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
            <tr><td>Porsche Informatik</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
            <tr><td>Usersnap</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
            <tr><td>Startrampe</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
            <tr><td>hello again</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
            <tr><td>smec</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
          </tbody>
        </table>
        <div class="fallback-note">📈 This data represents the distribution of events across different hosting organizations in our community.</div>
      </div>
    </div>
  </div>

  <div class="stat-section">
    <h3>🎤 Top 15 Speakers</h3>
    <div class="chart-container">
      <canvas id="topSpeakersChart"></canvas>
      <div id="topSpeakersFallback" style="display: none;">
        <div class="chart-title">🎤 Top Speakers</div>
        <table class="stats-table">
          <thead>
            <tr>
              <th>Speaker</th>
              <th>Presentations</th>
              <th>Visual Representation</th>
            </tr>
          </thead>
          <tbody>
          {% comment %} Speakers ordered by talk count, then by most recent appearance {% endcomment %}
          {% comment %} 3 talks (most recent first) {% endcomment %}
          <tr><td>Markus Adelsberger</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 45px;"></span> 3</td></tr>
          <tr><td>Martin Strigl</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 45px;"></span> 3</td></tr>
          {% comment %} 2 talks (most recent first) {% endcomment %}
          <tr><td>Matthias Steinbauer</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 30px;"></span> 2</td></tr>
          <tr><td>Alexander Lackner</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 30px;"></span> 2</td></tr>
          <tr><td>Katharina Sick</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 30px;"></span> 2</td></tr>
          <tr><td>Juliano Costa</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 30px;"></span> 2</td></tr>
          {% comment %} 1 talk (most recent speakers first) {% endcomment %}
          <tr><td>Simon Gartner</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 15px;"></span> 1</td></tr>
          <tr><td>Markus Gierlinger</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 15px;"></span> 1</td></tr>
          <tr><td>Christian Schabetsberger</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 15px;"></span> 1</td></tr>
          <tr><td>Siegfried Stumpfer</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 15px;"></span> 1</td></tr>
          <tr><td>Shahab Ganji</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 15px;"></span> 1</td></tr>
          <tr><td>Jan Wiesbauer</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 15px;"></span> 1</td></tr>
          <tr><td>Florian Arthofer</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 15px;"></span> 1</td></tr>
          <tr><td>Sebastian Huber</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 15px;"></span> 1</td></tr>
          <tr><td>Christoph Ruhsam</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 15px;"></span> 1</td></tr>
          </tbody>
        </table>
        <div class="fallback-note">🎤 This data shows which speakers have presented most often at our events, highlighting our active community contributors.</div>
      </div>
    </div>
  </div>

  <div class="stat-section">
    <h3>📊 Participant Trends</h3>
    <div class="chart-container">
      <canvas id="participantsTrendsChart"></canvas>
      <div id="participantsTrendsFallback" style="display: none;">
        <div class="chart-title">📊 Participants Trends</div>
        <table class="stats-table">
          <thead>
            <tr>
              <th>Date</th>
              <th>Event</th>
              <th>Participants</th>
              <th>Popularity</th>
            </tr>
          </thead>
          <tbody>
            {% for event in site.data.events %}
              {% assign part_str = event.participants | strip %}
              {% assign part_num = part_str | plus: 0 %}
              {% if part_str != '' and part_num > 0 %}
              <tr>
                <td>{{ event.date }}</td>
                <td>{{ event.title }}</td>
                <td class="number-cell">{{ part_num }}</td>
                <td><span class="host-bar" style="width: {{ part_num | divided_by: 2 }}px;"></span> {{ part_num }}</td>
              </tr>
              {% endif %}
            {% endfor %}
          </tbody>
        </table>
        <div class="fallback-note">📈 Participants data shows community engagement levels over time and helps us understand event popularity trends.</div>
      </div>
    </div>
  </div>
</div>

<div class="community-highlights">
  <div class="card">
    <h3>🚀 Community Impact</h3>
    <div class="highlight-grid">
      <div class="highlight-item">
        <div class="highlight-number">{% assign total_events = site.data.events | size %}{{ total_events }}</div>
        <div class="highlight-label">Total Events</div>
      </div>
      <div class="highlight-item">
        <div class="highlight-number">700+</div>
        <div class="highlight-label">Community members</div>
      </div>
      <div class="highlight-item">
        <div class="highlight-number">{% assign total_hosts = site.data.events | map: 'host' | uniq | size %}{{ total_hosts }}</div>
        <div class="highlight-label">Host Organizations</div>
      </div>
      <div class="highlight-item">
        {% assign all_speakers = "" | split: "|" %}
        {% for event in site.data.events %}
          {% if event.talks %}
            {% for talk in event.talks %}
              {% if talk.speaker and talk.speaker != '' %}
                {% assign all_speakers = all_speakers | push: talk.speaker %}
              {% endif %}
            {% endfor %}
          {% endif %}
        {% endfor %}
        {% assign unique_all_speakers = all_speakers | uniq | size %}
        <div class="highlight-number">{{ unique_all_speakers }}</div>
        <div class="highlight-label">Unique Speakers</div>
      </div>
      <div class="highlight-item">
        {% assign total_talks = 0 %}
        {% for event in site.data.events %}
          {% if event.talks %}
            {% assign total_talks = total_talks | plus: event.talks.size %}
          {% endif %}
        {% endfor %}
        <div class="highlight-number">{{ total_talks }}</div>
        <div class="highlight-label">Total Talks</div>
      </div>
    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
  const chartsStatus = document.getElementById('charts-status');
  const fallbackNotice = document.getElementById('fallback-notice');
  const fallbacks = {
    hostOrganizations: document.getElementById('hostOrganizationsFallback'),
    topSpeakers: document.getElementById('topSpeakersFallback'),
    participantsTrends: document.getElementById('participantsTrendsFallback')
  };

  chartsStatus.style.display = 'block';

  // Check if Chart.js loaded successfully
  if (typeof Chart === 'undefined') {
    showFallbacks();
    return;
  }

  try {
    createCharts();
  } catch (error) {
    console.error('Error creating charts:', error);
    showFallbacks();
  }

  function showFallbacks() {
    chartsStatus.style.display = 'none';
    fallbackNotice.style.display = 'block';
    Object.values(fallbacks).forEach(fb => fb.style.display = 'block');
  }

  function createCharts() {
    chartsStatus.style.display = 'none';

    // Host Organizations Chart
    const hostCtx = document.getElementById('hostOrganizationsChart');
    if (hostCtx) {
      new Chart(hostCtx, {
        type: 'bar',
        data: {
          labels: ['Gepardec', 'Cloudflight', 'Dynatrace', 'netcetera', 'karriere.at', 'Public Cloud Group', 'Runtastic', 'MIC', 'tractive', 'cloudxcelerate', 'eww IT and TEL', 'Porsche Informatik', 'Usersnap', 'Startrampe', 'hello again', 'smec'],
          datasets: [{
            label: 'Events Hosted',
            data: [3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            backgroundColor: 'rgba(102, 126, 234, 0.8)',
            borderColor: 'rgba(102, 126, 234, 1)',
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: false }
          },
          scales: {
            y: { beginAtZero: true }
          }
        }
      });
    }

    // Top Speakers Chart with correct chronological ordering
    const speakersCtx = document.getElementById('topSpeakersChart');
    if (speakersCtx) {
      new Chart(speakersCtx, {
        type: 'bar',
        data: {
          labels: ['Markus Adelsberger', 'Martin Strigl', 'Matthias Steinbauer', 'Alexander Lackner', 'Katharina Sick', 'Juliano Costa', 'Simon Gartner', 'Markus Gierlinger', 'Christian Schabetsberger', 'Siegfried Stumpfer', 'Shahab Ganji', 'Jan Wiesbauer', 'Florian Arthofer', 'Sebastian Huber', 'Christoph Ruhsam'],
          datasets: [{
            label: 'Presentations',
            data: [3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            backgroundColor: 'rgba(118, 75, 162, 0.8)',
            borderColor: 'rgba(118, 75, 162, 1)',
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: false }
          },
          scales: {
            y: { beginAtZero: true },
            x: {
              ticks: {
                maxRotation: 45,
                minRotation: 45
              }
            }
          }
        }
      });
    }

    // Participants Trends Chart with actual data
    const participantsCtx = document.getElementById('participantsTrendsChart');
    if (participantsCtx) {
      new Chart(participantsCtx, {
        type: 'line',
        data: {
          labels: ['Mar 2022', 'Oct 2022', 'Nov 2022', 'Jan 2023', 'Feb 2023', 'Mar 2023', 'Apr 2023', 'May 2023', 'Jun 2023', 'Sep 2023', 'Jan 2024', 'Mar 2024', 'Apr 2024', 'Jun 2024', 'Sep 2024', 'Oct 2024', 'Nov 2024', 'Jan 2025', 'Feb 2025', 'Mar 2025', 'Apr 2025', 'May 2025', 'Jul 2025'],
          datasets: [{
            label: 'Participants',
            data: [38, 35, 45, 43, 35, 25, 52, 37, 27, 41, 31, 39, 40, 22, 22, 27, 22, 33, 34, 29, 31, 27, 17],
            borderColor: 'rgba(102, 126, 234, 1)',
            backgroundColor: 'rgba(102, 126, 234, 0.1)',
            fill: true,
            tension: 0.4
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: false }
          },
          scales: {
            y: { 
              beginAtZero: true,
              max: 60
            },
            x: {
              ticks: {
                maxRotation: 45,
                minRotation: 45
              }
            }
          }
        }
      });
    }
  }
});
</script>
