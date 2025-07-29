---
layout: page
title: Statistics
permalink: /statistics/
---

## Community Statistics

Here you can find insights about our Cloud Native Computing Linz meetups including event timelines, hosting organizations, and participation trends.

<div id="charts-status" class="alert-info" style="display: none; padding: 15px; background-color: #d1ecf1; border: 1px solid #bee5eb; border-radius: 5px; margin: 20px 0;">
  <strong>📊 Loading interactive charts...</strong> If charts don't appear, static data tables will be shown instead.
</div>

<div id="fallback-notice" class="alert-warning" style="display: none; padding: 15px; background-color: #fff3cd; border: 1px solid #ffeaa7; border-radius: 5px; margin: 20px 0;">
  <strong>📋 Interactive charts unavailable:</strong> Displaying data in table format. Charts require external resources that may be blocked by network restrictions.
</div>

### Top 15 Host Organizations
<div class="chart-container">
  <canvas id="hostOrganizationsChart"></canvas>
  <div id="hostOrganizationsFallback" style="display: none;">
    <div class="chart-title">📊 Host Organizations</div>
    <table class="stats-table">
      <thead>
        <tr><th>Host Organization</th><th>Events Hosted</th><th>Visual</th></tr>
      </thead>
      <tbody>
        <tr><td>Dynatrace</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 30px;"></span> 3</td></tr>
        <tr><td>Cloudflight</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 30px;"></span> 3</td></tr>
        <tr><td>Gepardec</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 30px;"></span> 3</td></tr>
        <tr><td>Runtastic</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 20px;"></span> 2</td></tr>
        <tr><td>Public Cloud Group</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 20px;"></span> 2</td></tr>
        <tr><td>karriere.at</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 20px;"></span> 2</td></tr>
        <tr><td>netcetera</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 20px;"></span> 2</td></tr>
        <tr><td>tractive</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
        <tr><td>cloudxcelerate</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
        <tr><td>eww IT and TEL</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
        <tr><td>Porsche Informatik</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
        <tr><td>Usersnap</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
        <tr><td>Startrampe</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
        <tr><td>Tractive</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
        <tr><td>hello again</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
        <tr><td>smec</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
        <tr><td>MIC</td><td class="number-cell">1</td><td><span class="host-bar" style="width: 10px;"></span> 1</td></tr>
      </tbody>
    </table>
    <div class="fallback-note">📈 This data represents the distribution of events across different hosting organizations.</div>
  </div>
</div>

### Top 15 Speakers
<div class="chart-container">
  <canvas id="topSpeakersChart"></canvas>
  <div id="topSpeakersFallback" style="display: none;">
    <div class="chart-title">🎤 Top Speakers</div>
    <table class="stats-table">
      <thead>
        <tr><th>Speaker</th><th>Presentations</th><th>Visual</th></tr>
      </thead>
      <tbody>
      {% assign speakers = "" | split: "|" %}
      {% for event in site.data.events %}
        {% if event.talks %}
          {% for talk in event.talks %}
            {% if talk.speaker and talk.speaker != '' %}
              {% comment %} First replace all [, ], and quotes {% endcomment %}
              {% assign talk_speakers = talk.speaker | replace: '[', '' | replace: ']', '' | replace: '"', '' %}
              
              {% comment %} Replace all ampersands (both HTML entity and regular) with commas {% endcomment %}
              {% assign talk_speakers = talk_speakers | replace: '&amp;', ', ' | replace: ' & ', ', ' %}
              
              {% comment %} Split by comma and process each name {% endcomment %}
              {% assign speaker_parts = talk_speakers | split: ',' %}
              {% for part in speaker_parts %}
                {% assign single_speaker = part | strip %}
                {% if single_speaker != '' %}
                  {% assign speakers = speakers | push: single_speaker %}
                {% endif %}
              {% endfor %}
            {% endif %}
          {% endfor %}
        {% endif %}
      {% endfor %}
      {% assign unique_speakers = speakers | uniq %}
      {% assign speaker_rows = "" | split: "|" %}
      {% for speaker in unique_speakers %}
        {% assign count = 0 %}
        {% for s in speakers %}
          {% if s == speaker %}
            {% assign count = count | plus: 1 %}
          {% endif %}
        {% endfor %}
        {% assign speaker_rows = speaker_rows | push: speaker | append: '|||' | append: count %}
      {% endfor %}
      {% assign sorted_speaker_rows = speaker_rows | sort_natural | reverse %}
      {% for entry in sorted_speaker_rows %}
        {% assign parts = entry | split: '|||' %}
        {% assign speaker = parts[0] %}
        {% assign count = parts[1] %}
        <tr>
          <td>{{ speaker }}</td>
          <td class="number-cell">{{ count }}</td>
          <td><span class="host-bar" style="width: {{ count | times: 10 }}px;"></span> {{ count }}</td>
        </tr>
      {% endfor %}
      </tbody>
    </table>
    <div class="fallback-note">🎤 This data shows which speakers have presented most often at our events.</div>
  </div>
</div>

### Participants Trends
<div class="chart-container">
  <canvas id="participantsTrendsChart"></canvas>
  <div id="participantsTrendsFallback" style="display: none;">
    <div class="chart-title">📊 Participants Trends</div>
    <table class="stats-table">
      <thead>
        <tr><th>Date</th><th>Event</th><th>Participants</th><th>Popularity</th></tr>
      </thead>
      <tbody>
        {% for event in site.data.events reversed %}
          {% assign part_str = event.participants | strip %}
          {% assign part_num = part_str | plus: 0 %}
          {% if part_str != '' and part_num > 0 %}
          <tr>
            <td>{{ event.date }}</td>
            <td><strong>{{ event.title }}</strong></td>
            <td class="number-cell">{{ part_num }}</td>
            <td>
              {% if part_num >= 50 %}
                <span class="host-bar" style="width: 50px; background-color: #28a745;"></span> High
              {% elsif part_num >= 30 %}
                <span class="host-bar" style="width: 30px; background-color: #ffc107;"></span> Medium
              {% else %}
                <span class="host-bar" style="width: 20px; background-color: #17a2b8;"></span> Low
              {% endif %}
            </td>
          </tr>
          {% endif %}
        {% endfor %}
      </tbody>
    </table>
    <div class="fallback-note">📈 Participants data shows community engagement levels over time.</div>
  </div>
</div>

### Event Frequency by Month
<div class="chart-container">
  <canvas id="monthlyFrequencyChart"></canvas>
  <div id="monthlyFrequencyFallback" style="display: none;">
    <div class="chart-title">📅 Event Frequency by Month</div>
    <table class="stats-table">
      <thead>
        <tr><th>Month</th><th>Events Count</th><th>Activity Level</th></tr>
      </thead>
      <tbody>
        <tr><td>January</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 20px; background-color: #17a2b8;"></span> Low</td></tr>
        <tr><td>February</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 30px; background-color: #ffc107;"></span> Medium</td></tr>
        <tr><td>March</td><td class="number-cell">4</td><td><span class="host-bar" style="width: 40px; background-color: #28a745;"></span> High</td></tr>
        <tr><td>April</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 30px; background-color: #ffc107;"></span> Medium</td></tr>
        <tr><td>May</td><td class="number-cell">4</td><td><span class="host-bar" style="width: 40px; background-color: #28a745;"></span> High</td></tr>
        <tr><td>June</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 30px; background-color: #ffc107;"></span> Medium</td></tr>
        <tr><td>July</td><td class="number-cell">2</td><td><span class="host-bar" style="width: 20px; background-color: #17a2b8;"></span> Low</td></tr>
        <tr><td>August</td><td class="number-cell">0</td><td><span class="host-bar" style="width: 5px; background-color: #dc3545;"></span> None</td></tr>
        <tr><td>September</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 30px; background-color: #ffc107;"></span> Medium</td></tr>
        <tr><td>October</td><td class="number-cell">4</td><td><span class="host-bar" style="width: 40px; background-color: #28a745;"></span> High</td></tr>
        <tr><td>November</td><td class="number-cell">3</td><td><span class="host-bar" style="width: 30px; background-color: #ffc107;"></span> Medium</td></tr>
        <tr><td>December</td><td class="number-cell">0</td><td><span class="host-bar" style="width: 5px; background-color: #dc3545;"></span> None</td></tr>
      </tbody>
    </table>
    <div class="fallback-note">🗓️ Most active months are March, May, and October. Summer and winter months typically have fewer events.</div>
  </div>
</div>

### Recordings and Slides

Many of our events are recorded and slides are available. You can find these resources on the individual event pages or in our [slides repository]({{ site.baseurl }}/slides/).

<div id="recordings-list">
{% for event in site.data.events reversed %}
  {% if event.talks %}
    {% for talk in event.talks %}
      {% if talk.recording or talk.file %}
        <div class="recording-item">
          <strong>{{ event.date }}</strong> - {{ talk.title }} ({{ talk.speaker }})
          {% if talk.recording %}
            <a href="{{ talk.recording }}" target="_blank">🎥 Recording</a>
          {% endif %}
          {% if talk.file %}
            <a href="{{ site.baseurl }}{{ talk.file }}" target="_blank">📄 Slides</a>
          {% endif %}
        </div>
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
</div>

<!-- Try multiple CDNs for Chart.js -->
<script>
document.addEventListener('DOMContentLoaded', function() {
// Function to load scripts with fallback
function loadScript(src, callback, errorCallback) {
  const script = document.createElement('script');
  script.src = src;
  script.onload = callback;
  script.onerror = errorCallback;
  document.head.appendChild(script);
}

// Try loading Chart.js from multiple sources
const chartJsSources = [
  'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js',
  'https://unpkg.com/chart.js@3.9.1/dist/chart.min.js',
  'https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js'
];

let currentSourceIndex = 0;

function tryLoadChartJs() {
  // Show loading status
  var chartsStatus = document.getElementById('charts-status');
  if (chartsStatus) chartsStatus.style.display = 'block';
  
  if (currentSourceIndex >= chartJsSources.length) {
    // All CDNs failed, show fallback tables
    showFallbackTables();
    return;
  }
  
  loadScript(
    chartJsSources[currentSourceIndex],
    function() {
      // Chart.js loaded successfully, try to load date adapter
      loadScript(
        'https://cdnjs.cloudflare.com/ajax/libs/chartjs-adapter-date-fns/2.0.0/chartjs-adapter-date-fns.bundle.min.js',
        function() {
          // Both Chart.js and date adapter loaded
          if (chartsStatus) chartsStatus.style.display = 'none';
          initializeCharts();
        },
        function() {
          // Date adapter failed, initialize charts without time scales
          if (chartsStatus) chartsStatus.style.display = 'none';
          initializeChartsWithoutTime();
        }
      );
    },
    function() {
      // This CDN failed, try next one
      currentSourceIndex++;
      tryLoadChartJs();
    }
  );
}

// Prepare data from Jekyll
const eventsData = [
  {% for event in site.data.events %}
  {
    id: {{ event.id }},
    title: "{{ event.title | escape }}",
    date: "{{ event.date }}",
    host: "{{ event.host | escape }}",
    registrations: "{{ event.registrations | default: 0 | escape }}",
    participants: "{{ event.participants | default: '' }}",
    talks: [
      {% if event.talks %}
        {% for talk in event.talks %}
          {% if talk.speaker and talk.speaker != '' %}
          {
            title: "{{ talk.title | escape }}",
            speaker: "{{ talk.speaker | escape }}"
          }{% unless forloop.last %},{% endunless %}
          {% endif %}
        {% endfor %}
      {% endif %}
    ]
  }{% unless forloop.last %},{% endunless %}
  {% endfor %}
];

function showFallbackTables() {
  // Show fallback notice
  var chartsStatus = document.getElementById('charts-status');
  var fallbackNotice = document.getElementById('fallback-notice');
  if (chartsStatus) chartsStatus.style.display = 'none';
  if (fallbackNotice) fallbackNotice.style.display = 'block';
  
  // Fallback: Show static tables instead of charts
  var ids = [
    ['hostOrganizationsChart', 'hostOrganizationsFallback'],
    ['topSpeakersChart', 'topSpeakersFallback'],
    ['participantsTrendsChart', 'participantsTrendsFallback'],
    ['monthlyFrequencyChart', 'monthlyFrequencyFallback']
  ];
  ids.forEach(function(pair) {
    var chart = document.getElementById(pair[0]);
    var fallback = document.getElementById(pair[1]);
    if (chart) chart.style.display = 'none';
    if (fallback) fallback.style.display = 'block';
  });
}

function initializeChartsWithoutTime() {
  // Initialize charts without time scales (for when date adapter fails)
  if (typeof Chart === 'undefined') {
    showFallbackTables();
    return;
  }

  try {
    // Process data for charts
    const processEventsData = (events) => {
      // Host frequency data (exclude 'online' and sort desc)
      const hostCount = {};
      events.forEach(event => {
        if (event.host && event.host !== '' && event.host.toLowerCase() !== 'online') {
          hostCount[event.host] = (hostCount[event.host] || 0) + 1;
        }
      });
      // Sort hosts by count desc
      const sortedHosts = Object.entries(hostCount)
        .sort((a, b) => b[1] - a[1])
        .slice(0,15);
      const hostLabels = sortedHosts.map(([host]) => host);
      const hostData = sortedHosts.map(([, count]) => count);

      // Top speakers data
      const speakerCount = {};
      events.forEach(event => {
        if (event.talks && event.talks.length > 0) {
          event.talks.forEach(talk => {
            if (talk.speaker) {
              // Handle array or string format
              // First, ensure we're working with a string
              const speakerStr = String(talk.speaker);
              
              // Decode any HTML entities (like &amp;)
              const div = document.createElement('div');
              div.innerHTML = speakerStr;
              const decodedStr = div.textContent || div.innerText || speakerStr;
              
              // Remove brackets and quotes (for array format)
              const strippedStr = decodedStr.replace(/^\[|\]$/g, '').replace(/"/g, '');
              
              // Replace all ampersand variations with commas for consistent splitting
              const normalizedStr = strippedStr.replace(/\s*&\s*/g, ', ');
              
              // Split by comma and process
              const speakers = normalizedStr
                .split(',')
                .map(s => s.trim())      // Trim whitespace
                .filter(s => s);         // Remove empty strings
              
              // Count each speaker
              speakers.forEach(speaker => {
                if (speaker) {
                  speakerCount[speaker] = (speakerCount[speaker] || 0) + 1;
                }
              });
            }
          });
        }
      });
      
      // Sort speakers by count desc
      const sortedSpeakers = Object.entries(speakerCount)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 15); // Get top 20 speakers for better visualization
      const speakerLabels = sortedSpeakers.map(([speaker]) => speaker);
      const speakerData = sortedSpeakers.map(([, count]) => count);

      // Participants trends (strict numeric filtering)
      const participantsData = events
        .filter(event => {
          // Only include events where participants is a valid number
          if (!event.participants) return false;
          
          // Convert to string and check if it contains digits
          const participantsStr = String(event.participants);
          const numericValue = participantsStr.replace(/[^\d]/g, '');
          
          // Only accept if it has digits and converts to a valid number > 0
          return numericValue.length > 0 && !isNaN(Number(numericValue)) && Number(numericValue) > 0;
        })
        .map(event => ({
          x: event.date,
          y: parseInt(String(event.participants).replace(/[^\d]/g, ''), 10)
        }));

      // Monthly frequency
      const monthlyCount = {};
      events.forEach(event => {
        const month = new Date(event.date).getMonth();
        const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        const monthName = monthNames[month];
        monthlyCount[monthName] = (monthlyCount[monthName] || 0) + 1;
      });

      return {
        hostLabels,
        hostData,
        speakerLabels,
        speakerData,
        participants: participantsData,
        monthly: monthlyCount
      };
    };

    const chartData = processEventsData(eventsData);

    // Test speaker name processing
    function testSpeakerProcessing() {
      const testCases = [
        { input: 'John Doe', expected: ['John Doe'] },
        { input: 'John Doe & Jane Smith', expected: ['John Doe', 'Jane Smith'] },
        { input: 'John Doe &amp; Jane Smith', expected: ['John Doe', 'Jane Smith'] },
        { input: 'John Doe, Jane Smith', expected: ['John Doe', 'Jane Smith'] },
        { input: 'John Doe & Jane Smith, Bob Johnson', expected: ['John Doe', 'Jane Smith', 'Bob Johnson'] },
        { input: '[\"John Doe & Jane Smith\"]', expected: ['John Doe', 'Jane Smith'] },
        { input: 'John Doe & Jane Smith & Bob Johnson', expected: ['John Doe', 'Jane Smith', 'Bob Johnson'] }
      ];
      
      const resultsDiv = document.getElementById('speaker-test-results');
      resultsDiv.innerHTML = '<table class="debug-table" style="width:100%; border-collapse: collapse;">' +
        '<tr style="background: #e9ecef;"><th style="text-align:left; padding:8px;">Input</th>' +
        '<th style="text-align:left; padding:8px;">Processed Result</th>' +
        '<th style="text-align:left; padding:8px;">Expected</th>' +
        '<th style="text-align:center; padding:8px;">Pass</th></tr>';
      
      testCases.forEach(test => {
        // Process the speaker string
        const div = document.createElement('div');
        div.innerHTML = test.input;
        const decodedStr = div.textContent || div.innerText || test.input;
        const strippedStr = decodedStr.replace(/^\[|\]$/g, '').replace(/"/g, '');
        const normalizedStr = strippedStr.replace(/\s*&\s*/g, ', ');
        const processed = normalizedStr
          .split(',')
          .map(s => s.trim())
          .filter(s => s);
        
        // Check if the result matches expected
        const pass = JSON.stringify(processed) === JSON.stringify(test.expected);
        
        // Add to the results table
        resultsDiv.querySelector('table').innerHTML += 
          `<tr style="border-bottom: 1px solid #dee2e6;">
            <td style="padding:8px;">${test.input}</td>
            <td style="padding:8px;">${JSON.stringify(processed)}</td>
            <td style="padding:8px;">${JSON.stringify(test.expected)}</td>
            <td style="padding:8px; text-align:center; color:${pass ? 'green' : 'red'};font-weight:bold;">
              ${pass ? '✓' : '✗'}
            </td>
          </tr>`;
      });
      
      resultsDiv.querySelector('table').innerHTML += '</table>';
    }
    
    // Run the test when the page loads
    document.addEventListener('DOMContentLoaded', testSpeakerProcessing);

    // Chart configuration options
    const commonOptions = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: true
        }
      }
    };

    // Host Organizations Chart
    const hostCtx = document.getElementById('hostOrganizationsChart').getContext('2d');
    new Chart(hostCtx, {
      type: 'bar',
      data: {
        labels: chartData.hostLabels,
        datasets: [{
          label: 'Events Hosted',
          data: chartData.hostData,
          backgroundColor: 'rgba(255, 99, 132, 0.6)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1
        }]
      },
      options: {
        ...commonOptions,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Number of Events'
            },
            ticks: {
              stepSize: 1,
              precision: 0
            }
          },
          x: {
            title: {
              display: true,
              text: 'Host Organization'
            }
          }
        }
      }
    });
    
    // Top Speakers Chart
    const speakersCtx = document.getElementById('topSpeakersChart').getContext('2d');
    new Chart(speakersCtx, {
      type: 'bar',
      data: {
        labels: chartData.speakerLabels,
        datasets: [{
          label: 'Presentations Given',
          data: chartData.speakerData,
          backgroundColor: 'rgba(54, 162, 235, 0.6)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1
        }]
      },
      options: {
        ...commonOptions,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Number of Presentations'
            },
            ticks: {
              stepSize: 1,
              precision: 0
            }
          },
          x: {
            title: {
              display: true,
              text: 'Speaker'
            }
          }
        }
      }
    });

    // Participants Trends Chart
    if (chartData.participants.length > 0) {
      const participantsCtx = document.getElementById('participantsTrendsChart').getContext('2d');
      new Chart(participantsCtx, {
        type: 'line',
        data: {
          labels: chartData.participants.map(e => e.x),
          datasets: [{
            label: 'Participants',
            data: chartData.participants.map(e => e.y),
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: true
          }]
        },
        options: {
          ...commonOptions,
          scales: {
            x: {
              type: 'category',
              title: {
                display: true,
                text: 'Date'
              },
              labels: chartData.participants.map(e => e.x)
            },
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: 'Number of Participants'
              },
              ticks: {
                stepSize: 1,
                precision: 0
              }
            }
          }
        }
      });
    }

    // Monthly Frequency Chart
    const monthlyCtx = document.getElementById('monthlyFrequencyChart').getContext('2d');
    new Chart(monthlyCtx, {
      type: 'doughnut',
      data: {
        labels: Object.keys(chartData.monthly),
        datasets: [{
          data: Object.values(chartData.monthly),
          backgroundColor: [
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 205, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)',
            'rgba(255, 159, 64, 0.6)',
            'rgba(199, 199, 199, 0.6)',
            'rgba(83, 102, 255, 0.6)',
            'rgba(255, 99, 255, 0.6)',
            'rgba(99, 255, 132, 0.6)',
            'rgba(255, 132, 99, 0.6)',
            'rgba(132, 99, 255, 0.6)'
          ]
        }]
      },
      options: {
        ...commonOptions,
        plugins: {
          ...commonOptions.plugins,
          title: {
            display: true,
            text: 'Events Distribution by Month'
          }
        }
      }
    });
  } catch (error) {
    console.error('Error creating charts without time scale:', error);
    showFallbackTables();
  }
}

function initializeCharts() {
  // Initialize charts with time scales (when date adapter is available)
  if (typeof Chart === 'undefined') {
    showFallbackTables();
    return;
  }

  try {
    // Process data for charts
    const processEventsData = (events) => {
      // Host frequency data (exclude 'online' and sort desc)
      const hostCount = {};
      events.forEach(event => {
        if (event.host && event.host !== '' && event.host.toLowerCase() !== 'online') {
          hostCount[event.host] = (hostCount[event.host] || 0) + 1;
        }
      });
      // Sort hosts by count desc
      const sortedHosts = Object.entries(hostCount)
        .sort((a, b) => b[1] - a[1]);
      const hostLabels = sortedHosts.map(([host]) => host);
      const hostData = sortedHosts.map(([, count]) => count);
      
      // Top speakers data
      const speakerCount = {};
      events.forEach(event => {
        if (event.talks && event.talks.length > 0) {
          event.talks.forEach(talk => {
            if (talk.speaker) {
              // Handle array or string format
              // First, decode HTML entities (like &amp; to &)
              const decodedSpeaker = talk.speaker.replace(/&amp;/g, '&');
              
              // Then clean up brackets, quotes
              const cleanedSpeakerStr = decodedSpeaker.replace(/[\[\]"]/g, '');
              
              // Replace all ampersands with commas for consistent splitting
              const normalizedStr = cleanedSpeakerStr.replace(/\s*&\s*/g, ', ');
              
              // Split by comma and process each name
              const speakers = normalizedStr
                .split(',')
                .map(s => s.trim())
                .filter(s => s && s.length > 0);
              
              // Count each speaker
              speakers.forEach(speaker => {
                if (speaker) {
                  speakerCount[speaker] = (speakerCount[speaker] || 0) + 1;
                }
              });
            }
          });
        }
      });
      
      // Sort speakers by count desc
      const sortedSpeakers = Object.entries(speakerCount)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 20); // Get top 20 speakers for better visualization
      const speakerLabels = sortedSpeakers.map(([speaker]) => speaker);
      const speakerData = sortedSpeakers.map(([, count]) => count);

      // Participants trends (strict numeric filtering)
      // Get participants data with proper chronological order (oldest to newest)
      const participantsData = events
        .filter(event => {
          // Only include events where participants is a valid number
          if (!event.participants) return false;
          
          // Convert to string and check if it contains digits
          const participantsStr = String(event.participants);
          const numericValue = participantsStr.replace(/[^\d]/g, '');
          
          // Only accept if it has digits and converts to a valid number > 0
          return numericValue.length > 0 && !isNaN(Number(numericValue)) && Number(numericValue) > 0;
        })
        .map(event => ({
          x: event.date,
          y: parseInt(String(event.participants).replace(/[^\d]/g, ''), 10)
        }));    // Monthly frequency
      const monthlyCount = {};
      events.forEach(event => {
        const month = new Date(event.date).getMonth();
        const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        const monthName = monthNames[month];
        monthlyCount[monthName] = (monthlyCount[monthName] || 0) + 1;
      });

      return {
        hostLabels,
        hostData,
        speakerLabels,
        speakerData,
        participants: participantsData,
        monthly: monthlyCount
      };
    };

    const chartData = processEventsData(eventsData);

    // Test speaker name processing
    function testSpeakerProcessing() {
      const testCases = [
        { input: 'John Doe', expected: ['John Doe'] },
        { input: 'John Doe & Jane Smith', expected: ['John Doe', 'Jane Smith'] },
        { input: 'John Doe &amp; Jane Smith', expected: ['John Doe', 'Jane Smith'] },
        { input: 'John Doe, Jane Smith', expected: ['John Doe', 'Jane Smith'] },
        { input: 'John Doe & Jane Smith, Bob Johnson', expected: ['John Doe', 'Jane Smith', 'Bob Johnson'] },
        { input: '[\"John Doe & Jane Smith\"]', expected: ['John Doe', 'Jane Smith'] },
        { input: 'John Doe & Jane Smith & Bob Johnson', expected: ['John Doe', 'Jane Smith', 'Bob Johnson'] }
      ];
      
      const resultsDiv = document.getElementById('speaker-test-results');
      resultsDiv.innerHTML = '<table class="debug-table" style="width:100%; border-collapse: collapse;">' +
        '<tr style="background: #e9ecef;"><th style="text-align:left; padding:8px;">Input</th>' +
        '<th style="text-align:left; padding:8px;">Processed Result</th>' +
        '<th style="text-align:left; padding:8px;">Expected</th>' +
        '<th style="text-align:center; padding:8px;">Pass</th></tr>';
      
      testCases.forEach(test => {
        // Process the speaker string
        const div = document.createElement('div');
        div.innerHTML = test.input;
        const decodedStr = div.textContent || div.innerText || test.input;
        const strippedStr = decodedStr.replace(/^\[|\]$/g, '').replace(/"/g, '');
        const normalizedStr = strippedStr.replace(/\s*&\s*/g, ', ');
        const processed = normalizedStr
          .split(',')
          .map(s => s.trim())
          .filter(s => s);
        
        // Check if the result matches expected
        const pass = JSON.stringify(processed) === JSON.stringify(test.expected);
        
        // Add to the results table
        resultsDiv.querySelector('table').innerHTML += 
          `<tr style="border-bottom: 1px solid #dee2e6;">
            <td style="padding:8px;">${test.input}</td>
            <td style="padding:8px;">${JSON.stringify(processed)}</td>
            <td style="padding:8px;">${JSON.stringify(test.expected)}</td>
            <td style="padding:8px; text-align:center; color:${pass ? 'green' : 'red'};font-weight:bold;">
              ${pass ? '✓' : '✗'}
            </td>
          </tr>`;
      });
      
      resultsDiv.querySelector('table').innerHTML += '</table>';
    }
    
    // Run the test when the page loads
    document.addEventListener('DOMContentLoaded', testSpeakerProcessing);

    // Chart configuration options
    const commonOptions = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: true
        }
      }
    };

    // Host Organizations Chart
    const hostCtx = document.getElementById('hostOrganizationsChart').getContext('2d');
    new Chart(hostCtx, {
      type: 'bar',
      data: {
        labels: chartData.hostLabels,
        datasets: [{
          label: 'Events Hosted',
          data: chartData.hostData,
          backgroundColor: 'rgba(255, 99, 132, 0.6)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1
        }]
      },
      options: {
        ...commonOptions,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Number of Events'
            },
            ticks: {
              stepSize: 1,
              precision: 0
            }
          },
          x: {
            title: {
              display: true,
              text: 'Host Organization'
            }
          }
        }
      }
    });

    // Top Speakers Chart
    const speakersCtx = document.getElementById('topSpeakersChart').getContext('2d');
    new Chart(speakersCtx, {
      type: 'bar',
      data: {
        labels: chartData.speakerLabels,
        datasets: [{
          label: 'Presentations Given',
          data: chartData.speakerData,
          backgroundColor: 'rgba(54, 162, 235, 0.6)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1
        }]
      },
      options: {
        ...commonOptions,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Number of Presentations'
            },
            ticks: {
              stepSize: 1,
              precision: 0
            }
          },
          x: {
            title: {
              display: true,
              text: 'Speaker'
            }
          }
        }
      }
    });

    // Participants Trends Chart with time scale
    if (chartData.participants.length > 0) {
      const participantsCtx = document.getElementById('participantsTrendsChart').getContext('2d');
      new Chart(participantsCtx, {
        type: 'line',
        data: {
          datasets: [{
            label: 'Participants',
            data: chartData.participants,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: true
          }]
        },
        options: {
          ...commonOptions,
          scales: {
            x: {
              type: 'time',
              time: {
                parser: 'YYYY-MM-DD',
                tooltipFormat: 'MMM DD, YYYY'
              },
              title: {
                display: true,
                text: 'Date'
              }
            },
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: 'Number of Participants'
              },
              ticks: {
                stepSize: 1,
                precision: 0
              }
            }
          }
        }
      });
    }

    // Monthly Frequency Chart
    const monthlyCtx = document.getElementById('monthlyFrequencyChart').getContext('2d');
    new Chart(monthlyCtx, {
      type: 'doughnut',
      data: {
        labels: Object.keys(chartData.monthly),
        datasets: [{
          data: Object.values(chartData.monthly),
          backgroundColor: [
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 205, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)',
            'rgba(255, 159, 64, 0.6)',
            'rgba(199, 199, 199, 0.6)',
            'rgba(83, 102, 255, 0.6)',
            'rgba(255, 99, 255, 0.6)',
            'rgba(99, 255, 132, 0.6)',
            'rgba(255, 132, 99, 0.6)',
            'rgba(132, 99, 255, 0.6)'
          ]
        }]
      },
      options: {
        ...commonOptions,
        plugins: {
          ...commonOptions.plugins,
          title: {
            display: true,
            text: 'Events Distribution by Month'
          }
        }
      }
    });
  } catch (error) {
    console.error('Error creating charts with time scale:', error);
    // Fallback to non-time charts
    initializeChartsWithoutTime();
  }
}

// Start loading Chart.js
tryLoadChartJs();
});
</script>

<style>
.chart-container {
  position: relative;
  height: 400px;
  margin: 20px 0;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fdfdfd;
}

.chart-container h4 {
  margin-top: 0;
  color: #333;
  border-bottom: 2px solid #007bff;
  padding-bottom: 8px;
}

.recording-item {
  margin: 10px 0;
  padding: 10px;
  background-color: #f8f9fa;
  border-left: 4px solid #007bff;
  border-radius: 4px;
}

.recording-item a {
  margin-left: 10px;
  text-decoration: none;
  padding: 4px 8px;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  font-size: 0.9em;
}

.recording-item a:hover {
  background-color: #0056b3;
}

#recordings-list {
  max-height: 400px;
  overflow-y: auto;
  margin-top: 20px;
}

.stats-table {
  width: 100%;
  border-collapse: collapse;
  margin: 10px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-radius: 8px;
  overflow: hidden;
}

.stats-table th,
.stats-table td {
  border: 1px solid #ddd;
  padding: 12px 15px;
  text-align: left;
}

.stats-table th {
  background-color: #007bff;
  color: white;
  font-weight: bold;
  text-transform: uppercase;
  font-size: 0.9em;
  letter-spacing: 0.5px;
}

.stats-table tr:nth-child(even) {
  background-color: #f8f9fa;
}

.stats-table tr:hover {
  background-color: #e3f2fd;
  transition: background-color 0.2s ease;
}

.stats-table td:last-child {
  font-weight: bold;
  color: #007bff;
}

/* Visual indicators for data */
.stats-table .number-cell {
  text-align: center;
  font-family: 'Courier New', monospace;
  font-weight: bold;
  background-color: #e8f4fd;
}

.host-bar {
  display: inline-block;
  height: 20px;
  background-color: #007bff;
  margin-right: 8px;
  border-radius: 3px;
  vertical-align: middle;
}

.chart-title {
  font-size: 1.2em;
  font-weight: bold;
  margin-bottom: 15px;
  color: #333;
  text-align: center;
}

.fallback-note {
  font-style: italic;
  color: #666;
  text-align: center;
  margin-top: 15px;
  padding: 10px;
  background-color: #f0f8ff;
  border-radius: 5px;
  border: 1px solid #cce7ff;
}

.alert-info, .alert-warning {
  margin: 20px 0;
  padding: 15px;
  border-radius: 5px;
  font-weight: 500;
}

.alert-info {
  background-color: #d1ecf1;
  border: 1px solid #bee5eb;
  color: #0c5460;
}

.alert-warning {
  background-color: #fff3cd;
  border: 1px solid #ffeaa7;
  color: #856404;
}
</style>