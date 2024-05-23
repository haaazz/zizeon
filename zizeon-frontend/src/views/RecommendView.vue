<template>
  <div>
    <h1 class="text-center text-2xl font-bold text-green-600 sm:text-3xl mb-6 mt-12">
      ✨상품 추천✨
      </h1>
      <p class="text-center mb-8"> 각 상품명을 클릭하면 상세 정보 조회 페이지로 이동합니다.</p>

<div class="w-5/6 text-center flex space-x-6 mx-auto justify-around">
  <div class="border border-gray-400 p-2 rounded-lg">
    <h3 class="text-center text-xl font-bold text-green-600 sm:text-xl mb-6 mt-4">추천 예금 목록</h3>
        <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
          <thead class="ltr:text-left rtl:text-right">
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">회사명</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">상품명</th>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="deposit in recommendDeposits" :key="deposit.id">
            <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center">
              {{ deposit.kor_co_nm }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center">
              <RouterLink :to="{ name: 'DepositDetail', params: { id: deposit.id } }">
            {{ deposit.fin_prdt_nm }}
          </RouterLink>
            </td>
          </tr>
          </tbody>
        </table>
  </div>

  <div class="border border-gray-400 p-2 rounded-lg">
    <h3 class="text-center text-xl font-bold text-green-600 sm:text-xl mb-6 mt-4">추천 적금 목록</h3>
        <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
          <thead class="ltr:text-left rtl:text-right">
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">회사명</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">상품명</th>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="saving in recommendSavings" :key="saving.id">
            <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center">
              {{ saving.kor_co_nm }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center">
              <RouterLink :to="{ name: 'SavingDetail', params: { id: saving.id } }">
            {{ saving.fin_prdt_nm }}
          </RouterLink>
            </td>
          </tr>
          </tbody>
        </table>
  </div>

  </div>
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
