<template>
  <div>
    <h1>상품 상세 정보</h1>
  </div>

  <div v-if="deposit">
    <h3>금융상품명: {{ deposit.fin_prdt_nm }}</h3>
    <h3>금융회사명: {{ deposit.kor_co_nm }}</h3>
  </div>

  <form v-if="userstore.isLogin">
    <label for="balance"> 예치금: </label>
    <input type="number" id="balance" v-model="balance" />
    <button @click.prevent="open">가입</button>
  </form>

  <div v-for="option in options" :key="option.id">
    <hr />
    <p>저축금리:{{ option.intr_rate }}</p>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useDepositStore } from "@/stores/deposit";
import { useUserStore } from "@/stores/user";

const store = useDepositStore();
const route = useRoute();
const router = useRouter();
const userstore = useUserStore();

const deposit = ref(null);
const options = ref(null);
const balance = ref(0);

const open = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/products/deposit/${route.params.id}/open/`,
    data: {
      balance: balance.value,
    },
    headers: {
      Authorization: `Token ${userstore.loginUser.value.token}`,
    },
  })
    .then((response) => {
      userstore.getUserOpenedProducts()
      router.push({ name: "mypage" });
    })
    .catch((error) => {
      console.log(balance.value);
    });
};

const openedDeposits = ref([]);
const check = function (id) {
  return openedDeposits.value.some((deposit) => deposit.deposit === id);
};

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/products/deposit/${route.params.id}/`,
  })
    .then((res) => {
      deposit.value = res.data.deposit;
      options.value = res.data.options;
    })
    .catch((err) => console.log(err));
});
</script>

<style scoped></style>
