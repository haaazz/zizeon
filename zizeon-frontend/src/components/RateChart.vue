<!-- src/components/MyChart.vue -->
<template>
  <div class="charts">
    <Bar :data="depositChart" :options="chartOptions" />
    <Bar :data="savingChart" :options="chartOptions" />
  </div>
</template>

<script setup>
  import { useUserStore } from '@/stores/user'
  import { ref, computed } from 'vue'
  import { useDepositStore } from '@/stores/deposit'
  import { useSavingStore } from '@/stores/saving'
  import { Bar } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
  
  const store = useUserStore()
  const destore = useDepositStore()
  const sastore = useSavingStore()
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
  const savingIds = computed(() => store.loginUser.savings.map(item => item.saving))
  const savings = computed(() => sastore.savings.filter(item => savingIds.value.includes(item.id)))
  const savingNames = computed(() => savings.value.map(item => item.fin_prdt_nm))
  const savingOptions = computed(() => sastore.savingoptions.filter(item => savingIds.value.includes(item.saving)))
  const savingRates = computed(() => {
    const groupedSaving = savingOptions.value.reduce((acc, cur) => {
      if (!acc[cur.fin_prdt_cd]) {
        acc[cur.fin_prdt_cd] = []
      }
      acc[cur.fin_prdt_cd].push(cur.intr_rate)
      return acc
    }, {})
    const result = []
    for (const key in groupedSaving) {
      const avg = groupedSaving[key].reduce((acc, cur) => acc + cur, 0) / groupedSaving[key].length;
      result.push(avg) 
    }
    return result
  })
  const savingRates2 = computed(() => {
    const groupedSaving = savingOptions.value.reduce((acc, cur) => {
      if (!acc[cur.fin_prdt_cd]) {
        acc[cur.fin_prdt_cd] = []
      }
      acc[cur.fin_prdt_cd].push(cur.intr_rate2)
      return acc
    }, {})
    const result = []
    for (const key in groupedSaving) {
      const avg = groupedSaving[key].reduce((acc, cur) => acc + cur, 0) / groupedSaving[key].length;
      result.push(avg) 
    }
    return result
  })
  
  // Chart.js 모듈 등록
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

  const savingChart = {
    labels: savingNames.value,
    datasets: [
      {
        label: 'Data One',
        backgroundColor: '#16a34a',  // 여기야 여기!! 색깔 바꾸는 거 여기야!
        data: [40, 39, 10]
      },
      {
        label: 'Data Two',
        backgroundColor: '#facc15',  // 여기야 여기!! 색깔 바꾸는 거 여기야!
        data: [20, 30, 50]
      }
    ]
  }

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false
  }
</script>

<style scoped>
  .charts {
    width: 400px;
    height: 300px;
  }
</style>
  