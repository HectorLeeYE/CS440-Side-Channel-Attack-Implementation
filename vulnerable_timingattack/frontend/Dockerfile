FROM node:22-slim as build

WORKDIR /app

# Copy package.json & package-lock.json and install deps
COPY package*.json ./
RUN npm install
RUN npm install react-router-dom

# Copy the rest of the frontend code
COPY . .

# Build the React app
RUN npm run build

# Serve with http-server
FROM node:22-slim
WORKDIR /app

# Install http-server globally
RUN npm install -g http-server

# Copy build output from previous stage
COPY --from=build /app/dist .

# Expose port
EXPOSE 3000

# Start server
CMD ["http-server", "-p", "3000"]