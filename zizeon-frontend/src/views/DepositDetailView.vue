<template>
  <div>
    <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8 mt-20">
      <div class="mx-auto w-3/5">
        <h2
          class="text-center text-2xl font-bold text-green-600 sm:text-3xl mb-8"
        >
          상세 정보 조회 👀
        </h2>
        <hr />

        <div
          v-if="userstore.isLogin"
          class="flex items-end justify-evenly mb-3"
        >
          <form>
            <label
              for="balance"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white mt-3"
              >예치금</label
            >
            <input
              type="number"
              id="balance"
              v-model="balance"
              class="p-1 border rounded-lg"
            />
            <button
              @click.prevent="open"
              class="p-1 border rounded-lg bg-green-400"
            >
              상품 가입
            </button>
          </form>
          <div>
            <button
              @click.prevent="cancleDeposit"
              class="p-1 border rounded-lg bg-red-400"
            >
              가입 해지
            </button>
          </div>
        </div>
        <hr />
        <div>
          <div v-if="deposit" class="mt-8">
            <p class="mb-3">공시제출월: {{ deposit.dcls_month }}</p>
            <p class="mb-3">금융상품명: {{ deposit.fin_prdt_nm }}</p>
            <p class="mb-3">금융회사명: {{ deposit.kor_co_nm }}</p>
            <p class="mb-3">가입대상: {{ deposit.join_member }}</p>
            <p class="mb-3">가입방법: {{ deposit.join_way }}</p>
            <p class="mb-3">가입제한: {{ deposit.join_deny }}</p>
            <p class="mb-3">기타설명: {{ deposit.etc_note }}</p>
            <p class="mb-3">우대조건: {{ deposit.spcl_cnd }}</p>
            <p class="mb-3">만기후이자율: {{ deposit.mtrt_int }}</p>
          </div>
        </div>

        <hr />
        <h3
          class="text-center text-xl font-bold text-green-600 sm:text-xl mt-6 mb-6"
        >
          가입 옵션
        </h3>
        <div class="flex ml-2 mr-2 flex-wrap justify-around">
          <div
            v-for="option in options"
            :key="option.id"
            class="block w-2/5 mb-3 p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700"
          >
            <p class="font-normal text-gray-700 dark:text-gray-400">
              저축기간: {{ option.save_trm }}
            </p>
            <p class="font-normal text-gray-700 dark:text-gray-400">
              저축금리: {{ option.intr_rate }}
            </p>
            <p class="font-normal text-gray-700 dark:text-gray-400">
              최고우대금리: {{ option.intr_rate2 }}
            </p>
          </div>
        </div>
        <div class="text-center mt-8">
          <button
            @click="goBack"
            class="p-2 border rounded-lg bg-gray-300 hover:bg-gray-400"
          >
            뒤로가기
          </button>
        </div>
      </div>
    </div>
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
      userstore.getUserOpenedProducts();
      router.push({ name: "mypage" });
    })
    .catch((error) => {
      console.log(balance.value);
    });
};

const cancleDeposit = function () {
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
      userstore.getUserOpenedProducts();
      router.push({ name: "mypage" });
    })
    .catch((error) => {
      console.log(balance.value);
    });
};

const goBack = function () {
  router.back();
};

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
