import axios from "axios"

const API = axios.create({
  baseURL: "http://localhost:8000"
})

export const fetchAlerts = (jobId) =>
  API.get(`/alerts/${jobId}`)

export const uploadLogs = (file) => {
  const formData = new FormData()
  formData.append("file", file)

  return API.post("/logs/upload", formData)
}

export default API