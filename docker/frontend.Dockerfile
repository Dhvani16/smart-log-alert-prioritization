FROM node:22

WORKDIR /app

COPY frontend/log-dashboard/package*.json ./
RUN npm install

COPY frontend/log-dashboard .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]