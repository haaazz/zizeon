<template>
  <div>
    <h1>추천 상품 조회</h1>

    <h3>추천 예금 목록</h3>
    <ul>
      <li v-for="deposit in recommendDeposits" :key="deposit.id">
        <p>
          상품명:
          <RouterLink :to="{ name: 'DepositDetail', params: { id: deposit.id } }">
            {{ deposit.fin_prdt_nm }}
          </RouterLink>
        </p>
        <p>회사명: {{ deposit.kor_co_nm }}</p>
      </li>
    </ul>
    
    <h3>추천 적금 목록</h3>
    <ul>
      <li v-for="saving in recommendSavings" :key="saving.id">
        <p>
          상품명:
          <RouterLink :to="{ name: 'SavingDetail', params: { id: saving.id } }">
            {{ saving.fin_prdt_nm }}
          </RouterLink>
        </p>
        <p>회사명: {{ saving.kor_co_nm }}</p>
      </li>
    </ul>
  </div>
</template>

<script setup>
import axios from "axios"
import { onMounted, ref } from "vue"
import { useUserStore } from "@/stores/user"

const store = useUserStore()

const recommendSavings = ref([])
const recommendDeposits = ref([])

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/products/saving/recommend`,
  })
    .then((response) => {
      recommendSavings.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
    axios({
      method: "get",
      url: `${store.API_URL}/products/deposit/recommend`,
    })
      .then((response) => {
        recommendDeposits.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
})
</script>

<style scoped></style>
