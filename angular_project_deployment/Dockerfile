# Stage 1: Build the Angular application
FROM node:18-alpine AS build
WORKDIR /app

# Copy dependency definitions and install packages
COPY package*.json ./
RUN npm install

# Copy the entire application code and build the Angular app
COPY . .
RUN npm run build

# Stage 2: Create the final Nginx image
FROM nginx:latest

# Replace the main Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the custom server block (for HTTPS) into Nginx's conf.d directory
COPY default.conf /etc/nginx/conf.d/default.conf

# Create directory for SSL certificates and copy them in
RUN mkdir -p /etc/nginx/certs
COPY selfsigned.crt /etc/nginx/certs/selfsigned.crt
COPY selfsigned.key /etc/nginx/certs/selfsigned.key

# Remove the default Nginx website contents
RUN rm -rf /usr/share/nginx/html/*

# Copy the Angular build output from the build stage.
COPY --from=build /app/dist/website/ /usr/share/nginx/html/
# (Remove any extra copy of index.html if present.)

# Expose the internal port (4200) that Nginx is configured to use
EXPOSE 4200

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
