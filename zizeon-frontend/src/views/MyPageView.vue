<template>
  <div>
    <h1>마이페이지</h1>
    <button @click="ProfileEdit">회원 정보 수정</button>
    <h3>가입한 적금 목록</h3>
    <ul>
      <li v-for="saving in savings" :key="saving.id">
        <p v-for="s in savingsInfo(saving.saving)">
          상품명: <RouterLink :to="{ name: 'SavingDetail', params: { id: s.id } }">{{ s.fin_prdt_nm }}</RouterLink>
        </p>
        <p v-for="s in savingsInfo(saving.saving)">회사명: {{ s.kor_co_nm }}</p>
      </li>
    </ul>

    <h3>가입한 예금 목록</h3>
    <ul>
      <li v-for="deposit in deposits" :key="deposit.id">
        <p v-for="s in depositsInfo(deposit.deposit)">
          상품명: <RouterLink :to="{ name: 'DepositDetail', params: { id: s.id } }">{{ s.fin_prdt_nm }}</RouterLink>
        </p>
        <p v-for="s in depositsInfo(deposit.deposit)">회사명: {{ s.kor_co_nm }}</p>
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

  const store = useSavingStore()
  const userstore = useUserStore()
  const destore = useDepositStore()
  const router = useRouter()

  const savings = ref([])
  const deposits = ref([])

  const savingsInfo = function (pk) {
    return store.savings.filter((saving) => saving.id === pk)
  }

  const depositsInfo = function (pk) {
    return destore.deposits.filter((deposit) => deposit.id === pk)
  }

  const ProfileEdit = () => {
    router.push('/profileEdit')
  }

  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/accounts/products/`,
      headers: {
        Authorization: `Token ${userstore.token}`
      }
    })
    .then((response) => {
      savings.value = response.data.open_savings
      deposits.value = response.data.open_deposits
    })
    .catch((error) => {
      console.log(error)
    })
})

</script>

<style scoped>

</style>