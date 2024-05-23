<!-- src/components/MyChart.vue -->
<template>
    <div>
      <Bar :data="chartData" :options="chartOptions" />
    </div>
  </template>
  
  <script setup>
    import { Bar } from 'vue-chartjs';
    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
    
    // Chart.js 모듈 등록
    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
    
    const chartData = {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: '#16a34a',  // 여기야 여기!! 색깔 바꾸는 거 여기야!
          data: [40, 39, 10, 40, 39, 80, 40]
        },
        {
          label: 'Data Two',
          backgroundColor: '#facc15',  // 여기야 여기!! 색깔 바꾸는 거 여기야!
          data: [20, 30, 50, 60, 70, 90, 100]
        }
      ]
    }
  
    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false
    }
  </script>
  
  <style scoped>
  /* 필요한 스타일을 추가하세요 */
  </style>
  