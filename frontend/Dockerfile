# Use official Node.js image
FROM node:20-alpine

# Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set working directory
WORKDIR /app

# Change ownership of the working directory
RUN chown appuser:appgroup /app

# Copy package files first for better caching
COPY --chown=appuser:appgroup package*.json ./

# Install dependencies as root first (to avoid permission issues)
RUN npm install

# Change ownership of node_modules
RUN chown -R appuser:appgroup /app/node_modules

# Copy the rest of the application
COPY --chown=appuser:appgroup . .

# Switch to non-root user
USER appuser

# Expose the development port
EXPOSE 5173

# Command to run the application
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
