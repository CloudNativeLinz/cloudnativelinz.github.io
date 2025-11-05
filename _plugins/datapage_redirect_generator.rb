module Jekyll
  module DatapageRedirectGenerator
    class DataPageRedirect < Page
      def initialize(site, base, dir, data)
        @site = site
        @base = base
        @dir = dir
        @name = "index.html"

        self.process(@name)
        self.read_yaml(File.join(base, '_layouts'), 'redirect.html')
        
        self.data['redirect_to'] = data['redirect_to']
      end
    end

    class Generator < Jekyll::Generator
      safe true
      priority :low

      def generate(site)
        # Only run after the datapage generator has run
        return unless site.data['events']

        site.data['events'].each do |event|
          if event['redirect_from']
            event['redirect_from'].each do |redirect_path|
              # Remove leading slash if present
              clean_path = redirect_path.sub(/^\//, '')
              
              # Create redirect page
              redirect_page = DataPageRedirect.new(
                site, 
                site.source, 
                clean_path,
                {
                  'redirect_to' => "/events/meetup/#{event['slug']}/"
                }
              )
              
              site.pages << redirect_page
            end
          end
        end
      end
    end
  end
end