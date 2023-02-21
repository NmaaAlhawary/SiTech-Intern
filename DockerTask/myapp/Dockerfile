FROM node:16-alpine@sha256:25828d5c4ae9824273db9ca2e923da2d29bbae78f534e979f09eb99a2e812e94

# Create app directory
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./ 
RUN useradd -m nmaa 

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .
#make the port 8080 aviable to app
#EXPOSE 8080
USER nmaa
#start or run the app
#CMD [ "node", "server.js" ]

ENTRYPOINT [ "node", "server.js" ]
