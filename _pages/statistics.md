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
      <div style="text-align: center; margin-top: 2rem;">
        <a href="https://github.com/CloudNativeLinz/cloudnativelinz.github.io/issues/new?template=2-host-us.yaml" target="_blank" rel="noopener" class="btn btn-light">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11h-4v4h-2v-4H7v-2h4V7h2v4h4v2z"/>
          </svg>
          Become a Host
        </a>
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
      <div style="text-align: center; margin-top: 2rem;">
        <a href="https://github.com/CloudNativeLinz/cloudnativelinz.github.io/issues/new?template=1-submit-a-talk.yaml" target="_blank" rel="noopener" class="btn btn-light-secondary">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11h-4v4h-2v-4H7v-2h4V7h2v4h4v2z"/>
          </svg>
          Become a Speaker
        </a>
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

    // Generate dynamic data from Jekyll - only include past events
    const today = new Date();
    const eventsData = [
      {% for event in site.data.events %}
      {
        host: "{{ event.host | escape }}",
        date: "{{ event.date }}",
        participants: "{{ event.participants | strip }}",
        talks: [
          {% if event.talks %}
            {% for talk in event.talks %}
              {
                speaker: "{{ talk.speaker | escape }}"
              }{% unless forloop.last %},{% endunless %}
            {% endfor %}
          {% endif %}
        ]
      }{% unless forloop.last %},{% endunless %}
      {% endfor %}
    ].filter(event => {
      // Only include events that have already occurred
      const eventDate = new Date(event.date);
      return eventDate <= today;
    });

    // Process Host Organizations data
    const hostCounts = {};
    const hostLastEvent = {};
    
    eventsData.forEach(event => {
      if (event.host && event.host.trim() !== '' && event.host !== 'online') {
        hostCounts[event.host] = (hostCounts[event.host] || 0) + 1;
        // Track the most recent hosting date for this organization
        const eventDate = new Date(event.date);
        if (!hostLastEvent[event.host] || eventDate > hostLastEvent[event.host]) {
          hostLastEvent[event.host] = eventDate;
        }
      }
    });
    
    const hostEntries = Object.entries(hostCounts)
      .sort((a, b) => {
        // First sort by event count (descending)
        if (b[1] !== a[1]) {
          return b[1] - a[1];
        }
        // Then sort by most recent hosting date (descending - most recent first)
        const dateA = hostLastEvent[a[0]];
        const dateB = hostLastEvent[b[0]];
        return dateB - dateA;
      })
      .slice(0, 15);
    
    const hostLabels = hostEntries.map(entry => entry[0]);
    const hostData = hostEntries.map(entry => entry[1]);

    // Process Speakers data
    const speakerCounts = {};
    const speakerLastAppearance = {};
    
    eventsData.forEach(event => {
      event.talks.forEach(talk => {
        if (talk.speaker && talk.speaker.trim() !== '') {
          // Handle multiple speakers - split by & and clean up each name
          let speakerString = talk.speaker.trim();
          
          // Split by & or &amp; (in case of HTML encoding)
          const speakers = speakerString.split(/\s*&(?:amp;)?\s*/)
            .map(s => s.trim())
            .filter(s => s !== '' && s !== '&' && s !== '&amp;');
          
          speakers.forEach(speaker => {
            if (speaker && speaker.trim() !== '') {
              speakerCounts[speaker] = (speakerCounts[speaker] || 0) + 1;
              // Track the most recent appearance date for this speaker
              const eventDate = new Date(event.date);
              if (!speakerLastAppearance[speaker] || eventDate > speakerLastAppearance[speaker]) {
                speakerLastAppearance[speaker] = eventDate;
              }
            }
          });
        }
      });
    });
    
    const speakerEntries = Object.entries(speakerCounts)
      .sort((a, b) => {
        // First sort by presentation count (descending)
        if (b[1] !== a[1]) {
          return b[1] - a[1];
        }
        // Then sort by most recent appearance (descending - most recent first)
        const dateA = speakerLastAppearance[a[0]];
        const dateB = speakerLastAppearance[b[0]];
        return dateB - dateA;
      })
      .slice(0, 15);
    
    const speakerLabels = speakerEntries.map(entry => entry[0]);
    const speakerData = speakerEntries.map(entry => entry[1]);

    // Process Participants Trends data
    const participantsData = eventsData
      .filter(event => event.participants && event.participants.trim() !== '' && !isNaN(parseInt(event.participants)))
      .map(event => ({
        date: event.date,
        participants: parseInt(event.participants)
      }))
      .sort((a, b) => new Date(a.date) - new Date(b.date));
    
    const participantLabels = participantsData.map(item => {
      const date = new Date(item.date);
      return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short' });
    });
    const participantValues = participantsData.map(item => item.participants);

    // Host Organizations Chart
    const hostCtx = document.getElementById('hostOrganizationsChart');
    if (hostCtx) {
      // Create gradient for host organizations
      const hostGradient = hostCtx.getContext('2d').createLinearGradient(0, 0, 0, 400);
      hostGradient.addColorStop(0, 'rgba(102, 126, 234, 0.9)');
      hostGradient.addColorStop(0.5, 'rgba(67, 56, 202, 0.8)');
      hostGradient.addColorStop(1, 'rgba(79, 70, 229, 0.7)');
      
      const hostHoverGradient = hostCtx.getContext('2d').createLinearGradient(0, 0, 0, 400);
      hostHoverGradient.addColorStop(0, 'rgba(102, 126, 234, 1)');
      hostHoverGradient.addColorStop(0.5, 'rgba(67, 56, 202, 0.95)');
      hostHoverGradient.addColorStop(1, 'rgba(79, 70, 229, 0.9)');

      new Chart(hostCtx, {
        type: 'bar',
        data: {
          labels: hostLabels,
          datasets: [{
            label: 'Events Hosted',
            data: hostData,
            backgroundColor: hostGradient,
            borderColor: 'rgba(67, 56, 202, 1)',
            borderWidth: 2,
            borderRadius: 8,
            borderSkipped: false,
            hoverBackgroundColor: hostHoverGradient,
            hoverBorderColor: 'rgba(79, 70, 229, 1)',
            hoverBorderWidth: 3
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: 'rgba(17, 24, 39, 0.95)',
              titleColor: 'rgba(243, 244, 246, 1)',
              bodyColor: 'rgba(243, 244, 246, 1)',
              borderColor: 'rgba(102, 126, 234, 0.8)',
              borderWidth: 1,
              cornerRadius: 8,
              displayColors: false,
              callbacks: {
                label: function(context) {
                  return `${context.parsed.y} event${context.parsed.y !== 1 ? 's' : ''} hosted`;
                }
              }
            }
          },
          scales: {
            y: { 
              beginAtZero: true,
              ticks: {
                stepSize: 1,
                color: 'rgba(75, 85, 99, 0.8)',
                font: { size: 12 }
              },
              grid: {
                color: 'rgba(229, 231, 235, 0.5)',
                drawBorder: false
              }
            },
            x: {
              ticks: {
                color: 'rgba(75, 85, 99, 0.8)',
                font: { size: 11 },
                maxRotation: 45,
                minRotation: 45
              },
              grid: {
                display: false
              }
            }
          },
          interaction: {
            intersect: false,
            mode: 'index'
          },
          animation: {
            duration: 1000,
            easing: 'easeInOutQuart'
          }
        }
      });
    }

    // Top Speakers Chart
    const speakersCtx = document.getElementById('topSpeakersChart');
    if (speakersCtx) {
      // Create gradient for speakers
      const speakerGradient = speakersCtx.getContext('2d').createLinearGradient(0, 0, 0, 400);
      speakerGradient.addColorStop(0, 'rgba(168, 85, 247, 0.9)');
      speakerGradient.addColorStop(0.5, 'rgba(147, 51, 234, 0.8)');
      speakerGradient.addColorStop(1, 'rgba(126, 34, 206, 0.7)');
      
      const speakerHoverGradient = speakersCtx.getContext('2d').createLinearGradient(0, 0, 0, 400);
      speakerHoverGradient.addColorStop(0, 'rgba(168, 85, 247, 1)');
      speakerHoverGradient.addColorStop(0.5, 'rgba(147, 51, 234, 0.95)');
      speakerHoverGradient.addColorStop(1, 'rgba(126, 34, 206, 0.9)');

      new Chart(speakersCtx, {
        type: 'bar',
        data: {
          labels: speakerLabels,
          datasets: [{
            label: 'Presentations',
            data: speakerData,
            backgroundColor: speakerGradient,
            borderColor: 'rgba(147, 51, 234, 1)',
            borderWidth: 2,
            borderRadius: 8,
            borderSkipped: false,
            hoverBackgroundColor: speakerHoverGradient,
            hoverBorderColor: 'rgba(126, 34, 206, 1)',
            hoverBorderWidth: 3
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: 'rgba(17, 24, 39, 0.95)',
              titleColor: 'rgba(243, 244, 246, 1)',
              bodyColor: 'rgba(243, 244, 246, 1)',
              borderColor: 'rgba(168, 85, 247, 0.8)',
              borderWidth: 1,
              cornerRadius: 8,
              displayColors: false,
              callbacks: {
                label: function(context) {
                  return `${context.parsed.y} presentation${context.parsed.y !== 1 ? 's' : ''}`;
                }
              }
            }
          },
          scales: {
            y: { 
              beginAtZero: true,
              ticks: {
                stepSize: 1,
                color: 'rgba(75, 85, 99, 0.8)',
                font: { size: 12 }
              },
              grid: {
                color: 'rgba(229, 231, 235, 0.5)',
                drawBorder: false
              }
            },
            x: {
              ticks: {
                color: 'rgba(75, 85, 99, 0.8)',
                font: { size: 11 },
                maxRotation: 45,
                minRotation: 45
              },
              grid: {
                display: false
              }
            }
          },
          interaction: {
            intersect: false,
            mode: 'index'
          },
          animation: {
            duration: 1000,
            easing: 'easeInOutQuart'
          }
        }
      });
    }

    // Participants Trends Chart
    const participantsCtx = document.getElementById('participantsTrendsChart');
    if (participantsCtx) {
      new Chart(participantsCtx, {
        type: 'line',
        data: {
          labels: participantLabels,
          datasets: [{
            label: 'Participants',
            data: participantValues,
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
              max: Math.max(...participantValues) + 10
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
