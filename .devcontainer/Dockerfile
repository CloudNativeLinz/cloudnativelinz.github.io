# Alpine-based Ruby image for Jekyll
FROM ruby:3.4-alpine

# Install necessary packages for Alpine Linux
RUN apk add --no-cache \
    build-base \
    linux-headers \
    git \
    python3 \
    py3-pip \
    bash \
    sudo

# Create vscode user
RUN addgroup -g 1000 vscode && \
    adduser -D -u 1000 -G vscode vscode && \
    echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode && \
    chmod 0440 /etc/sudoers.d/vscode

# Set up environment variables for gem paths
ENV GEM_HOME="/home/vscode/.local/share/gem/ruby/3.4.0"
ENV PATH="/home/vscode/.local/share/gem/ruby/3.4.0/bin:${PATH}"

# Switch to vscode user
USER vscode
WORKDIR /workspaces