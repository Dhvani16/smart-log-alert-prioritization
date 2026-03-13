function AlertsTable({ alerts }) {

  return (

    <table className="table-auto w-full mt-6 border">

      <thead>

        <tr className="bg-gray-100">
          <th className="p-2">Log Level</th>
          <th className="p-2">Severity</th>
          <th className="p-2">Anomaly Score</th>
          <th className="p-2">Message</th>
        </tr>

      </thead>

      <tbody>

        {alerts.slice(0, 100).map((alert, index) => (

          <tr
            key={index}
            className={`border-t ${index % 2 === 0 ? "bg-white" : "bg-gray-50"}`}
          >

            <td className="p-2">{alert.log_level}</td>

            <td className="p-2">

              <span
                className={
                  alert.severity_level === "critical"
                    ? "text-red-600 font-bold"
                    : alert.severity_level === "medium"
                    ? "text-yellow-600 font-bold"
                    : "text-green-600 font-semibold"
                }
              >
                {alert.severity_level}
              </span>

            </td>

            <td className="p-2">
              {alert.anomaly_score.toFixed(3)}
            </td>

            <td className="p-2 text-sm">
              {alert.message}
            </td>

          </tr>

        ))}

      </tbody>

    </table>
  )
}

export default AlertsTable