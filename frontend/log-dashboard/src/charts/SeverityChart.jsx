import { Pie } from "react-chartjs-2"
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js"

ChartJS.register(ArcElement, Tooltip, Legend)

function SeverityChart({ critical, medium, low }) {

  const data = {

    labels: ["Critical", "Medium", "Low"],

    datasets: [
      {
        data: [critical, medium, low],
        backgroundColor: [
          "#ef4444",
          "#f59e0b",
          "#10b981"
        ]
      }
    ]
  }

  return (
    <div className="w-96">
      <Pie data={data} />
    </div>
  )
}

export default SeverityChart