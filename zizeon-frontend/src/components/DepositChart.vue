<!-- src/components/MyChart.vue -->
<template>
  <div class="charts">
    <Bar :data="depositChart" :options="chartOptions" />
  </div>
</template>

<script setup>
  import { useUserStore } from '@/stores/user'
  import { ref, computed } from 'vue'
  import { useDepositStore } from '@/stores/deposit'
  import { Bar } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
  
  const store = useUserStore()
  const destore = useDepositStore()

  const depositIds = computed(() => store.loginUser.deposits.map(item => item.deposit))
  const deposits = computed(() => destore.deposits.filter(item => depositIds.value.includes(item.id)))
  const depositNames = computed(() => deposits.value.map(item => item.fin_prdt_nm))
  const depositOptions = computed(() => destore.depositoptions.filter(item => depositIds.value.includes(item.deposit)))
  const depositRates = computed(() => {
    const groupedDeposit = depositOptions.value.reduce((acc, cur) => {
      if (!acc[cur.fin_prdt_cd]) {
        acc[cur.fin_prdt_cd] = []
      }
      acc[cur.fin_prdt_cd].push(cur.intr_rate)
      return acc
    }, {})
    const result = []
    for (const key in groupedDeposit) {
      const avg = groupedDeposit[key].reduce((acc, cur) => acc + cur, 0) / groupedDeposit[key].length;
      result.push(avg) 
    }
    return result
  })
  const depositRates2 = computed(() => {
    const groupedDeposit = depositOptions.value.reduce((acc, cur) => {
      if (!acc[cur.fin_prdt_cd]) {
        acc[cur.fin_prdt_cd] = []
      }
      acc[cur.fin_prdt_cd].push(cur.intr_rate2)
      return acc
    }, {})
    const result = []
    for (const key in groupedDeposit) {
      const avg = groupedDeposit[key].reduce((acc, cur) => acc + cur, 0) / groupedDeposit[key].length;
      result.push(avg) 
    }
    return result
  })
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
  const depositChart = {
    labels: depositNames.value,
    datasets: [
      {
        label: '저축금리',
        backgroundColor: '#16a34a',  // 여기야 여기!! 색깔 바꾸는 거 여기야!
        data: depositRates.value
      },
      {
        label: '최고우대금리',
        backgroundColor: '#facc15',  // 여기야 여기!! 색깔 바꾸는 거 여기야!
        data: depositRates2.value
      }
    ]
  }

  // const chartOptions = {
  //   responsive: true,
  //   maintainAspectRatio: false
  // }
</script>

<style scoped>
  /* .charts {
    width: 500px;
    height: 200px;
  } */
</style>
  