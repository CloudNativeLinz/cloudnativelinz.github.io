---
layout: page
title: Events
permalink: events/
---

{% include upcoming-events.html %}

## Past Events

<div class="events-grid">
{% for event in site.data.events reversed %}
 {% assign event_date = event.date | date: "%Y-%m-%d" %}
 {% assign today = site.time | date: "%Y-%m-%d" %}
  
 {% if event_date < today %}
  <article class="event-card" data-event-id="{{ event.id }}">
    <div class="event-banner">
      <img src="https://raw.githubusercontent.com/CloudNativeLinz/go-image-generator/main/artifacts/{{ event.id }}.jpg" 
           alt="{{ event.title }}" 
           loading="lazy"
           onerror="this.src='https://via.placeholder.com/400x200/1f2937/ffffff?text=Event+{{ event.id }}'"
      />
      <div class="event-overlay">
        <div class="event-date">
          {% if event_date == today %}
            <span class="today-badge">TODAY</span>
          {% else %}
            {{ event.date | date: "%b %d, %Y" }}
          {% endif %}
        </div>
        {% if event.host != nil and event.host != "" %}
          <div class="event-host">📍 {{ event.host }}</div>
        {% endif %}
      </div>
    </div>
    
    <div class="event-content">
      <h3 class="event-title">
        <a href="{{ event.title | datapage_url: 'meetup' | remove: '.html' }}">{{ event.title }}</a>
      </h3>
      
      {% if event.talks %}
        <div class="event-talks">
          {% for talk in event.talks limit:2 %}
            <div class="talk-item">
              <div class="talk-title">{{ talk.title }}</div>
              <div class="talk-speaker">
                <span class="emoji" style="font-style: normal;">👨‍💻</span>
                <span class="talk-speaker-name">{{ talk.speaker }}</span><br>
                {% if talk.file %}
                  <a href="{{ event.title | datapage_url: 'meetup' | remove: '.html' }}">
                    📎 Get the slides 
                  </a>
                {% endif %}
                 {% if talk.recording %}
                  <a href="{{ event.title | datapage_url: 'meetup' | remove: '.html' }}">
                    📺 Watch the recording
                  </a>
                {% endif %}
              </div>
            </div>
          {% endfor %}
          {% if event.talks.size > 2 %}
            <div class="talk-item more-talks">
              <div class="talk-title">+{{ event.talks.size | minus: 2 }} more talk{% if event.talks.size > 3 %}s{% endif %}</div>
            </div>
          {% endif %}
        </div>
      {% endif %}
      
      <div class="event-meta">
        {% if event.participants != "" %}
          <span class="meta-item">
            <svg class="icon" viewBox="0 0 20 20" fill="currentColor">
              <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3z"/>
            </svg>
            {{ event.participants }} cloud-natives participated
          </span>
        {% endif %}
        
         <a class="meta-link" href="{{ event.title | datapage_url: 'meetup' | remove: '.html' }}">Event details</a>


        {% if event.event_link %}
          <a href="{{ event.event_link }}" class="meta-link" target="_blank" rel="noopener">
            <svg class="icon" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z" clip-rule="evenodd"/>
            </svg>
            View on Meetup.com
          </a>
        {% endif %}
      </div>
    </div>
  </article>
 {% endif %}
{% endfor %}
</div>

<script>
// Add intersection observer for scroll animations
if ('IntersectionObserver' in window) {
  const cards = document.querySelectorAll('.event-card');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }, index * 100);
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '50px'
  });
  
  cards.forEach((card) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(card);
  });
}
</script>