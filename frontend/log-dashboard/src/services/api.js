import axios from "axios"

const API_BASE_URL = "http://localhost:8000"

const API = axios.create({
  baseURL: API_BASE_URL
})

export const fetchAlerts = (jobId) =>
  API.get(`/alerts/${jobId}`)

export const uploadLogs = (file) => {
  const formData = new FormData()
  formData.append("file", file)

  return API.post("/logs/upload", formData)
}

export default API