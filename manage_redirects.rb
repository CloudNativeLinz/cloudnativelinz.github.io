#!/usr/bin/env ruby
require 'yaml'
require 'fileutils'

# Function to create URL-friendly slug from title
def create_slug(title)
  title.downcase
       .gsub(/[^\w\s-]/, '') # Remove special chars except word chars, spaces, hyphens
       .gsub(/\s+/, '-')     # Replace spaces with hyphens
       .gsub(/-+/, '-')      # Replace multiple hyphens with single hyphen
       .strip                # Remove leading/trailing whitespace
       .gsub(/^-|-$/, '')    # Remove leading/trailing hyphens
end

# Load events data
events_file = '_data/events.yml'
backup_file = "#{events_file}.backup"

puts "Event Redirect Management Tool"
puts "=" * 50

# Create backup
FileUtils.cp(events_file, backup_file)
puts "✓ Created backup: #{backup_file}"

# Load events
events = YAML.load_file(events_file)

# Process each event
updated_count = 0
events.each do |event|
  # Generate slug if it doesn't exist
  unless event['slug']
    event['slug'] = create_slug(event['title'])
    puts "✓ Generated slug for event #{event['id']}: '#{event['slug']}'"
    updated_count += 1
  end
end

if updated_count > 0
  # Write back to file
  File.open(events_file, 'w') do |file|
    file.write(events.to_yaml)
  end
  puts "\n✓ Updated #{updated_count} events with new slugs"
else
  puts "\n✓ All events already have slugs"
end

puts "\n" + "=" * 50
puts "REDIRECT MANAGEMENT GUIDE"
puts "=" * 50

puts "\n📝 To add redirects when changing a title:"
puts "1. Keep the existing 'slug' field unchanged"
puts "2. Add a 'redirect_from' array with old URLs"
puts "\nExample YAML structure:"
puts <<~YAML
  - id: 34
    title: "New Updated Title"
    slug: "stable-slug-name"          # Keep this the same!
    redirect_from:
      - "/events/meetup/old-url-path"
      - "/events/meetup/34-cloud-native-computing-linz-meetup"
    date: "2024-10-21"
    # ... rest of event data
YAML

puts "\n🔄 Workflow for title changes:"
puts "1. Update the 'title' field in #{events_file}"
puts "2. Keep the 'slug' field unchanged"
puts "3. Add old URL to 'redirect_from' array"
puts "4. Run: bundle exec jekyll build"
puts "5. Test old URLs redirect to new content"

puts "\n⚠️  IMPORTANT:"
puts "- Never change existing slug values"
puts "- Always add old URLs to redirect_from when changing titles"
puts "- Test redirects locally before deploying"

puts "\n🧪 Testing commands:"
puts "bundle exec jekyll build    # Build the site"
puts "bundle exec jekyll serve    # Test locally"

puts "\nRedirect management complete! 🎉"