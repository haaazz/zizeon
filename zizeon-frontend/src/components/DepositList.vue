<template>
  <div class="content">
    <h1>예금</h1>
    <div>
      <label for="bankFilter">은행 선택: </label>
      <select id="bankFilter" v-model="selectedBank" @change="filterDeposits">
        <option value="">전체</option>
        <option v-for="bank in uniqueBanks" :key="bank" :value="bank">{{ bank }}</option>
      </select>
      <button @click="resetFiltersAndSorting">초기화</button>
    </div>
    <table>
      <thead>
        <tr>
          <th>번호</th>
          <th>상품명</th>
          <th>회사명</th>
          <th @click="sortDeposits(6)">6개월</th>
          <th @click="sortDeposits(12)">12개월</th>
          <th @click="sortDeposits(24)">24개월</th>
          <th @click="sortDeposits(36)">36개월</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="deposit in paginatedDeposits" :key="deposit.id">
          <td>{{ deposit.id }}</td>
          <td><RouterLink :to="{ name:'DepositDetail', params: { id: deposit.id } }">{{ deposit.fin_prdt_nm }}</RouterLink></td>
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ getInterestRate(deposit, 6) }}</td>
          <td>{{ getInterestRate(deposit, 12) }}</td>
          <td>{{ getInterestRate(deposit, 24) }}</td>
          <td>{{ getInterestRate(deposit, 36) }}</td>
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
const filteredDeposits = ref([])
const options = ref([])
const currentPage = ref(1)
const itemsPerPage = 15
const selectedBank = ref('')

const uniqueBanks = computed(() => {
  const banks = deposits.value.map(deposit => deposit.kor_co_nm)
  return [...new Set(banks)]
})

const filterDeposits = () => {
  if (selectedBank.value) {
    filteredDeposits.value = deposits.value.filter(deposit => deposit.kor_co_nm === selectedBank.value)
  } else {
    filteredDeposits.value = deposits.value
  }
  currentPage.value = 1
}

const getInterestRate = (deposit, term) => {
  const option = options.value.find(option => option.fin_prdt_cd === deposit.fin_prdt_cd && option.save_trm === term.toString())
  return option ? option.intr_rate : '-'
}

const totalPages = computed(() => {
  return Math.ceil(filteredDeposits.value.length / itemsPerPage)
})

const paginatedDeposits = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return filteredDeposits.value.slice(start, end)
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

const sortOrder = ref({
  6: null,
  12: null,
  24: null,
  36: null,
})

const sortDeposits = (term) => {
  const order = sortOrder.value[term] === 'asc' ? 'desc' : 'asc'
  sortOrder.value[term] = order

  filteredDeposits.value.sort((a, b) => {
    const aRate = parseFloat(getInterestRate(a, term)) || 0
    const bRate = parseFloat(getInterestRate(b, term)) || 0
    return order === 'asc' ? aRate - bRate : bRate - aRate
  })
}

const resetFiltersAndSorting = () => {
  selectedBank.value = '';
  sortOrder.value = {
    6: null,
    12: null,
    24: null,
    36: null,
  };
  currentPage.value = 1;
  filterDeposits();

  // 금리 정렬 초기화
  Object.keys(sortOrder.value).forEach(term => {
    sortOrder.value[term] = null;
  });

  // 예금 번호를 기준으로 정렬
  filteredDeposits.value.sort((a, b) => a.id - b.id);
};
onMounted(async () => {
  await store.getDeposit()
  deposits.value = store.deposits
  options.value = store.depositoptions
  filterDeposits()
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
