<template>
    <div class="content">
      <h1>예금</h1>
      <table>
        <thead>
          <tr>
            <th>번호</th>
            <th>상품명</th>
            <th>회사명</th>
            <th>6개월</th>
            <th>12개월</th>
            <th>24개월</th>
            <th>36개월</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="deposit in paginatedDeposits" :key="deposit.id">
            <td>{{ deposit.id }}</td>
            <td><RouterLink :to="{name:'DepositDetail', params: {id:deposit.id}}">{{ deposit.fin_prdt_nm }}</RouterLink></td>
            <td>{{ deposit.kor_co_nm }}</td>
            <td v-for="option in changeOption(deposit, 6)"><p>{{ option.intr_rate }}</p></td>
            <td v-for="option in changeOption(deposit, 12)"><p>{{ option.intr_rate }}</p></td>
            <td v-for="option in changeOption(deposit, 24)"><p>{{ option.intr_rate }}</p></td>
            <td v-for="option in changeOption(deposit, 36)"><p>{{ option.intr_rate }}</p></td>
          </tr>
        </tbody>
      </table>
      <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">이전</button>
        <span>{{ currentPage }} / {{ totalPages }}</span>
        <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
      </div>
    </div>
  </template>
  
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  import { useDepositStore } from '@/stores/deposit'
  import { RouterLink } from 'vue-router'
  
  const store = useDepositStore()
  const deposits = ref([])
  const options = ref([])
  const currentPage = ref(1)
  // 한 페이지에 15개 상품씩만 출력
  const itemsPerPage = 15
  
  // 페이지네이션 -> 올림 처리하기위해 ceil 사용
  const totalPages = computed(() => {
    return Math.ceil(deposits.value.length / itemsPerPage)
  })
  
  const changeOption = function (deposit, trm) {
      console.log(options.value)
      return options.value.filter((option) => option.deposit == deposit.id && option.save_trm == trm)
  }

  const paginatedDeposits = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage
    const end = start + itemsPerPage
    return deposits.value.slice(start, end)
  })
  
  const nextPage = () => {
    if (currentPage.value < totalPages.value) {
      currentPage.value++
    }
  }
  
  const prevPage = () => {
    if (currentPage.value > 1) {
      currentPage.value--
    }
  }
  
  onMounted(async () => {
    await store.getDeposit()
    deposits.value = store.deposits
    options.value = store.depositoptions
  })
  </script>
  
  
  <style scoped>
  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  table {
    width: 80%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
  }
  
  th {
    background-color: #f2f2f2;
  }
  
  .pagination {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  button {
    padding: 5px 10px;
    cursor: pointer;
  }
  
  button:disabled {
    cursor: not-allowed;
    opacity: 0.5;
  }
  </style>
  
  