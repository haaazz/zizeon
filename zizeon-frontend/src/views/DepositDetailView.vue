<template>
  <div>
    <h1>상품 상세 정보</h1>
  </div>

  <div>
    <div v-if="deposit">
      <p>공시제출월: {{ deposit.dcls_month }}</p>
      <p>금융상품명: {{ deposit.fin_prdt_nm }}</p>
      <p>금융회사명: {{ deposit.kor_co_nm }}</p>
      <p>가입대상: {{ deposit.join_member }}</p>
      <p>가입방법: {{ deposit.join_way }}</p>
      <p>가입제한: {{ deposit.join_deny }}</p>
      <p>기타설명: {{ deposit.etc_note }}</p>
      <p>우대조건: {{ deposit.spcl_cnd }}</p>
      <p>만기후이자율: {{ deposit.mtrt_int }}</p>
    </div>


    <form v-if="userstore.isLogin" >

      <label for="balance">예치금: </label>
      <input type="number" id="balance" v-model="balance" />
      <button @click="open">가입</button>

    </form>

    <div>
      <button @click="cancleDeposit">해지</button>
    </div>
  </div>

    <div v-for="option in options" :key="option.id">
      <hr />
      <p>저축기간: {{ option.save_trm }}</p>
      <p>저축금리: {{ option.intr_rate }}</p>
      <p>최고우대금리: {{ option.intr_rate2 }}</p>
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
      Authorization: `Token ${userstore.loginUser.token}`,
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

const cancleDeposit = function(){
  axios({
    method: "delete",
    url: `${store.API_URL}/products/deposit/${route.params.id}/delete/`,
    data: {
      balance: balance.value,
    },
    headers: {
      Authorization: `Token ${userstore.loginUser.token}`,
    },
  })
    .then((response) => {
      userstore.getUserOpenedProducts()
      router.push({ name: "mypage" });
    })
    .catch((error) => {
      console.log(balance.value);
    });
}

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/products/deposit/${route.params.id}/`,
  })
    .then((res) => {
      deposit.value = res.data.deposit;
      options.value = res.data.option;
    })
    .catch((err) => console.log(err));
});
</script>

<style scoped></style>
