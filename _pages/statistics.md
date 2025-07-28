---
layout: page
title: Statistics
permalink: /statistics/
---

## Community Statistics

Here you can find insights about our Cloud Native Computing Linz meetups including event timelines, hosting organizations, and participation trends.

### Events Over Time
<div class="chart-container">
  <canvas id="eventsTimelineChart"></canvas>
  <div id="eventsTimelineFallback" style="display: none;">
    <table class="stats-table">
      <thead>
        <tr><th>Date</th><th>Event</th><th>Host</th></tr>
      </thead>
      <tbody>
        {% for event in site.data.events reversed limit:10 %}
        <tr>
          <td>{{ event.date }}</td>
          <td>{{ event.title }}</td>
          <td>{{ event.host }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
    <p><em>Recent 10 events shown. Full timeline would display {{ site.data.events | size }} total events.</em></p>
  </div>
</div>

### Host Organizations
<div class="chart-container">
  <canvas id="hostOrganizationsChart"></canvas>
  <div id="hostOrganizationsFallback" style="display: none;">
    <table class="stats-table">
      <thead>
        <tr><th>Host Organization</th><th>Events Hosted</th></tr>
      </thead>
      <tbody>
        <tr><td>online</td><td>8</td></tr>
        <tr><td>Dynatrace</td><td>3</td></tr>
        <tr><td>Cloudflight</td><td>3</td></tr>
        <tr><td>Gepardec</td><td>3</td></tr>
        <tr><td>Runtastic</td><td>2</td></tr>
        <tr><td>Public Cloud Group</td><td>2</td></tr>
        <tr><td>karriere.at</td><td>2</td></tr>
        <tr><td>tractive</td><td>1</td></tr>
        <tr><td>cloudxcelerate</td><td>1</td></tr>
        <tr><td>eww IT and TEL</td><td>1</td></tr>
        <tr><td>netcetera</td><td>2</td></tr>
        <tr><td>Porsche Informatik</td><td>1</td></tr>
        <tr><td>Usersnap</td><td>1</td></tr>
        <tr><td>Startrampe</td><td>1</td></tr>
        <tr><td>Tractive</td><td>1</td></tr>
        <tr><td>hello again</td><td>1</td></tr>
        <tr><td>smec</td><td>1</td></tr>
        <tr><td>MIC</td><td>1</td></tr>
      </tbody>
    </table>
  </div>
</div>

### Registration Trends
<div class="chart-container">
  <canvas id="registrationTrendsChart"></canvas>
  <div id="registrationTrendsFallback" style="display: none;">
    <table class="stats-table">
      <thead>
        <tr><th>Date</th><th>Event</th><th>Registrations</th></tr>
      </thead>
      <tbody>
        {% for event in site.data.events reversed %}
          {% if event.registrations and event.registrations != '' %}
          <tr>
            <td>{{ event.date }}</td>
            <td>{{ event.title }}</td>
            <td>{{ event.registrations }}</td>
          </tr>
          {% endif %}
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>

### Event Frequency by Month
<div class="chart-container">
  <canvas id="monthlyFrequencyChart"></canvas>
  <div id="monthlyFrequencyFallback" style="display: none;">
    <table class="stats-table">
      <thead>
        <tr><th>Month</th><th>Events Count</th></tr>
      </thead>
      <tbody>
        <tr><td>January</td><td>2</td></tr>
        <tr><td>February</td><td>3</td></tr>
        <tr><td>March</td><td>4</td></tr>
        <tr><td>April</td><td>3</td></tr>
        <tr><td>May</td><td>4</td></tr>
        <tr><td>June</td><td>3</td></tr>
        <tr><td>July</td><td>2</td></tr>
        <tr><td>August</td><td>0</td></tr>
        <tr><td>September</td><td>3</td></tr>
        <tr><td>October</td><td>4</td></tr>
        <tr><td>November</td><td>3</td></tr>
        <tr><td>December</td><td>0</td></tr>
      </tbody>
    </table>
    <p><em>Note: Most active months are March, May, and October. Summer and winter months typically have fewer events.</em></p>
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

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
// Prepare data from Jekyll
const eventsData = [
  {% for event in site.data.events %}
  {
    id: {{ event.id }},
    title: "{{ event.title | escape }}",
    date: "{{ event.date }}",
    host: "{{ event.host | escape }}",
    registrations: {{ event.registrations | default: 0 }},
    participants: "{{ event.participants | default: '' }}"
  }{% unless forloop.last %},{% endunless %}
  {% endfor %}
];

// Check if Chart.js is available
if (typeof Chart === 'undefined') {
  // Fallback: Show static tables instead of charts
  document.getElementById('eventsTimelineChart').style.display = 'none';
  document.getElementById('eventsTimelineFallback').style.display = 'block';
  
  document.getElementById('hostOrganizationsChart').style.display = 'none';
  document.getElementById('hostOrganizationsFallback').style.display = 'block';
  
  document.getElementById('registrationTrendsChart').style.display = 'none';
  document.getElementById('registrationTrendsFallback').style.display = 'block';
  
  document.getElementById('monthlyFrequencyChart').style.display = 'none';
  document.getElementById('monthlyFrequencyFallback').style.display = 'block';
} else {
  // Process data for charts
  const processEventsData = (events) => {
    // Events timeline data
    const timelineData = events.map(event => ({
      x: event.date,
      y: 1,
      title: event.title,
      host: event.host
    }));

    // Host frequency data
    const hostCount = {};
    events.forEach(event => {
      if (event.host && event.host !== '') {
        hostCount[event.host] = (hostCount[event.host] || 0) + 1;
      }
    });

    // Registration trends (filter out non-numeric values)
    const registrationData = events
      .filter(event => event.registrations && !isNaN(event.registrations))
      .map(event => ({
        x: event.date,
        y: parseInt(event.registrations)
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
      timeline: timelineData,
      hosts: hostCount,
      registrations: registrationData,
      monthly: monthlyCount
    };
  };

  const chartData = processEventsData(eventsData);

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

  try {
    // Events Timeline Chart
    const timelineCtx = document.getElementById('eventsTimelineChart').getContext('2d');
    new Chart(timelineCtx, {
      type: 'scatter',
      data: {
        datasets: [{
          label: 'Events',
          data: chartData.timeline,
          backgroundColor: 'rgba(54, 162, 235, 0.6)',
          borderColor: 'rgba(54, 162, 235, 1)',
          pointRadius: 8,
          pointHoverRadius: 10
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
            display: false
          }
        },
        plugins: {
          ...commonOptions.plugins,
          tooltip: {
            callbacks: {
              label: function(context) {
                const event = context.raw;
                return [event.title, `Hosted by: ${event.host}`];
              }
            }
          }
        }
      }
    });

    // Host Organizations Chart
    const hostCtx = document.getElementById('hostOrganizationsChart').getContext('2d');
    new Chart(hostCtx, {
      type: 'bar',
      data: {
        labels: Object.keys(chartData.hosts),
        datasets: [{
          label: 'Events Hosted',
          data: Object.values(chartData.hosts),
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

    // Registration Trends Chart
    if (chartData.registrations.length > 0) {
      const registrationCtx = document.getElementById('registrationTrendsChart').getContext('2d');
      new Chart(registrationCtx, {
        type: 'line',
        data: {
          datasets: [{
            label: 'Registrations',
            data: chartData.registrations,
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
                text: 'Number of Registrations'
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
    console.error('Error creating charts:', error);
    // Fallback for any chart creation errors
    document.getElementById('eventsTimelineChart').style.display = 'none';
    document.getElementById('eventsTimelineFallback').style.display = 'block';
    
    document.getElementById('hostOrganizationsChart').style.display = 'none';
    document.getElementById('hostOrganizationsFallback').style.display = 'block';
    
    document.getElementById('registrationTrendsChart').style.display = 'none';
    document.getElementById('registrationTrendsFallback').style.display = 'block';
    
    document.getElementById('monthlyFrequencyChart').style.display = 'none';
    document.getElementById('monthlyFrequencyFallback').style.display = 'block';
  }
}
</script>

<style>
.chart-container {
  position: relative;
  height: 400px;
  margin: 20px 0;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
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
}

.stats-table th,
.stats-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.stats-table th {
  background-color: #f2f2f2;
  font-weight: bold;
}

.stats-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.stats-table tr:hover {
  background-color: #f5f5f5;
}
</style>