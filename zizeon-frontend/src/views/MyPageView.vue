<template>
  <div>
    <div  class="ml-1 mr-1 max-w-screen-xl px-4 py-10 sm:px-6 lg:px-2 rounded-lg p-4 shadow-lg mt-8">
    <h1 class="text-center text-2xl font-bold text-green-600 sm:text-3xl">마이페이지</h1>

      <p>{{ userstore.loginUser.nickname }}</p>
      <p>{{ userstore.loginUser.username }}</p>
      <p>{{ userstore.loginUser.age }}</p>
      <p>{{ userstore.loginUser.job }}</p>
      <p>{{ userstore.loginUser.income }}</p>
      <p>{{ userstore.loginUser.gender }}</p>
      <p>{{ userstore.loginUser.email }}</p>

    <div class="flex gap-x-8 justify-center">
    <button @click="ProfileEdit" class="mt-8 inline-block rounded bg-green-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-green-700 focus:outline-none focus:ring focus:ring-yellow-400"
    >정보수정</button>
<button
class="mt-8 inline-block rounded bg-green-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-green-700 focus:outline-none focus:ring focus:ring-yellow-400"
              @click="logout"
            >
              로그아웃
            </button>
  </div>
</div>

    <h3>가입한 적금 목록</h3>
    <ul>
      <li v-for="saving in userstore.loginUser.savings" :key="saving.id">
        <p v-for="s in savingsInfo(saving.saving)">
          상품명: <RouterLink :to="{ name: 'SavingDetail', params: { id: s.id } }">{{ s.fin_prdt_nm }}</RouterLink>
        </p>
        <p v-for="s in savingsInfo(saving.saving)">회사명: {{ s.kor_co_nm }}</p>
      </li>
    </ul>
    <h5>금리 비교 그래프</h5>
    <DepositChart />

    <h3>가입한 예금 목록</h3>
    <ul>
      <li v-for="deposit in userstore.loginUser.deposits" :key="deposit.id">
        <p v-for="s in depositsInfo(deposit.deposit)">
          상품명: <RouterLink :to="{ name: 'DepositDetail', params: { id: s.id } }">{{ s.fin_prdt_nm }}</RouterLink>
        </p>
        <p v-for="s in depositsInfo(deposit.deposit)">회사명: {{ s.kor_co_nm }}</p>
      </li>
    </ul>
    <h5>금리 비교 그래프</h5>
    <SavingChart />

    <hr>

    <h3>추천 예금 목록</h3>
    <ul>
      <li v-for="deposit in recommendDeposits" :key="deposit.id">
        <p>상품명: <RouterLink :to="{ name: 'DepositDetail', params: { id: deposit.id } }">{{ deposit.fin_prdt_nm }}</RouterLink></p>
        <p>회사명: {{ deposit.kor_co_nm }}</p>
      </li>
    </ul>

    <h3>추천 적금 목록</h3>
    <ul>
      <li v-for="saving in recommendSavings" :key="saving.id">
        <p>상품명: <RouterLink :to="{ name: 'SavingDetail', params: { id: saving.id } }">{{ saving.fin_prdt_nm }}</RouterLink></p>
        <p>회사명: {{ saving.kor_co_nm }}</p>
      </li>
    </ul>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { useSavingStore } from '@/stores/saving'
  import { useDepositStore } from '@/stores/deposit'
  import { useUserStore } from '@/stores/user'
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import DepositChart from '@/components/DepositChart.vue'
  import SavingChart from '@/components/SavingChart.vue'

  const store = useSavingStore()
  const userstore = useUserStore()
  const destore = useDepositStore()
  const router = useRouter()

  const savingsInfo = function (pk) {
    return store.savings.filter((saving) => saving.id === pk)
  }

  const depositsInfo = function (pk) {
    return destore.deposits.filter((deposit) => deposit.id === pk)
  }

  const ProfileEdit = () => {
    router.push('/profileEdit')
  }

  const recommendDeposits = ref([])
  const recommendSavings = ref([])

  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/accounts/recommend/`,
      headers: {
        Authorization: `Token ${userstore.loginUser.token}`,
      },
    })
    .then((response) => {
      recommendDeposits.value = response.data.deposit
      recommendSavings.value = response.data.saving
    })
    .catch((error) => {
      console.log(error)
    })
  })
</script>

<style scoped>
  h3 {
    font-size: 20pt;
    margin: 10px 0;
  }
  h5 {
    font-size: 15pt;
    margin: 5px 0;
  }
</style>