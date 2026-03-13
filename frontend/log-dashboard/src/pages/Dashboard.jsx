import { useEffect, useState } from "react"
import { fetchAlerts } from "../services/api"
import SeverityChart from "../charts/SeverityChart"
import AlertsTable from "../components/AlertsTable"

function Dashboard() {

  const [alerts, setAlerts] = useState([])

  useEffect(() => {
    fetchAlerts(1).then(res => {
      console.log("API RESPONSE:", res.data)
      setAlerts(res.data)
    })
  }, [])

  const criticalCount = alerts.filter(a => a.severity_level === "critical").length
  const mediumCount = alerts.filter(a => a.severity_level === "medium").length
  const lowCount = alerts.filter(a => a.severity_level === "low").length

  return (

    <div className="p-8">

      <h1 className="text-2xl font-bold mb-4">
        Smart Log Monitoring Dashboard
      </h1>

      <SeverityChart
        critical={criticalCount}
        medium={mediumCount}
        low={lowCount}
      />

      <AlertsTable alerts={alerts} />

    </div>
  )
}

export default Dashboard