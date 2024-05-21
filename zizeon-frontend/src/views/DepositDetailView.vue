<template>
    <div>
      <h1>상품 상세 정보</h1>
    </div>
    <div v-if="deposit">
        <p>{{ deposit.fin_prdt_nm }}</p>
    </div>
    <div v-for="option in options">
        <p>{{ option.intr_rate }}</p>
    </div>
</template>

<script setup>

import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useDepositStore } from '@/stores/deposit'

const store = useDepositStore()
const route = useRoute()

const deposit = ref(null)
const options = ref(null)


onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/products/deposit/${route.params.id}/`
    })
    .then((res) => {
        deposit.value = res.data.deposit
        options.value = res.data.options
        console.log(deposit.value)
    })
    .catch(err => console.log(err))
    })


</script>

<style scoped>

</style>