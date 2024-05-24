<template>
  <div>
    <div
      class="mx-auto max-w-screen-xl px-4 py-10 sm:px-6 lg:px-2 rounded-lg p-4 shadow-lg mt-8"
    >
      <h1 class="text-center text-2xl font-bold text-green-600 sm:text-3xl">
        마이페이지
      </h1>

      <div class="text-center mt-10">
        <p>이름 : {{ userstore.loginUser.username }}</p>
        <p>닉네임 : {{ userstore.loginUser.nickname }}</p>
        <p>나이 : {{ userstore.loginUser.age }}</p>
        <p>직업 : {{ userstore.loginUser.job }}</p>
        <p>수입 : {{ userstore.loginUser.income }}</p>
        <p>성별 : {{ userstore.loginUser.gender }}</p>
        <p>이메일 : {{ userstore.loginUser.email }}</p>
      </div>
      <div class="flex gap-x-8 justify-center">
        <button
          @click="ProfileEdit"
          class="mt-8 inline-block rounded bg-green-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-green-700 focus:outline-none focus:ring focus:ring-yellow-400"
        >
          정보수정
        </button>
        <button
          class="mt-8 inline-block rounded bg-green-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-green-700 focus:outline-none focus:ring focus:ring-yellow-400"
          @click="logout"
        >
          로그아웃
        </button>

        <button
          class="mt-8 inline-block rounded bg-red-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-green-700 focus:outline-none focus:ring focus:ring-yellow-400"
          @click="exit"
        >
          회원탈퇴
        </button>
      </div>
    </div>

    <div class="w-5/6 text-center flex space-x-6 mx-auto justify-around mt-8">
      <div class="shadow-lg p-2 rounded-lg">
        <h3 class="text-center text-m sm:text-m mb-6 mt-4">
          개인 맞춤 추천 예금
        </h3>

        <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
          <thead class="ltr:text-left rtl:text-right">
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
              회사명
            </th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
              상품명
            </th>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="deposit in recommendDeposits" :key="deposit.id">
              <td
                class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
              >
                {{ deposit.kor_co_nm }}
              </td>
              <td
                class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
              >
                <RouterLink
                  :to="{ name: 'DepositDetail', params: { id: deposit.id } }"
                  >{{ deposit.fin_prdt_nm }}</RouterLink
                >
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="shadow-lg p-2 rounded-lg">
        <h3 class="text-center text-m sm:text-m mb-6 mt-4">
          개인 맞춤 추천 적금
        </h3>
        <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
          <thead class="ltr:text-left rtl:text-right">
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
              회사명
            </th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
              상품명
            </th>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="saving in recommendSavings" :key="saving.id">
              <td
                class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
              >
                {{ saving.kor_co_nm }}
              </td>
              <td
                class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
              >
                <RouterLink
                  :to="{ name: 'SavingDetail', params: { id: saving.id } }"
                >
                  {{ saving.fin_prdt_nm }}
                </RouterLink>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="w-full text-center flex mx-auto mt-8">
      <div class="shadow-lg p-2 rounded-lg w-1/2 ml-8 mr-8 bg-white">
        <h3>가입한 예금 목록</h3>
        <hr />

        <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
          <thead class="ltr:text-left rtl:text-right">
            <tr>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                회사명
              </th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                상품명
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr
              v-for="deposit in userstore.loginUser.deposits"
              :key="deposit.id"
            >
              <td
                class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
                v-for="s in depositsInfo(deposit.deposit)"
              >
                {{ s.kor_co_nm }}
              </td>
              <td
                class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
                v-for="s in depositsInfo(deposit.deposit)"
              >
                <RouterLink
                  :to="{ name: 'DepositDetail', params: { id: s.id } }"
                  >{{ s.fin_prdt_nm }}</RouterLink
                >
              </td>
            </tr>
          </tbody>
        </table>
        <hr />
        <h5>금리 비교 그래프</h5>
        <DepositChart />
      </div>

      <div class="shadow-lg p-2 rounded-lg w-1/2 ml-8 mr-8 bg-white">
        <h3>가입한 적금 목록</h3>
        <hr />
        <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
          <thead class="ltr:text-left rtl:text-right">
            <tr>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                회사명
              </th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                상품명
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="saving in userstore.loginUser.savings" :key="saving.id">
              <td
                class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
                v-for="s in savingsInfo(saving.saving)"
              >
                {{ s.kor_co_nm }}
              </td>
              <td
                class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
                v-for="s in savingsInfo(saving.saving)"
              >
                <RouterLink
                  :to="{ name: 'SavingDetail', params: { id: s.id } }"
                >
                  {{ s.fin_prdt_nm }}
                </RouterLink>
              </td>
            </tr>
          </tbody>
        </table>
        <hr />
        <h5>금리 비교 그래프</h5>
        <SavingChart />
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { useSavingStore } from "@/stores/saving";
import { useDepositStore } from "@/stores/deposit";
import { useUserStore } from "@/stores/user";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import DepositChart from "@/components/DepositChart.vue";
import SavingChart from "@/components/SavingChart.vue";

const store = useSavingStore();
const userstore = useUserStore();
const destore = useDepositStore();
const router = useRouter();

const savingsInfo = function (pk) {
  return store.savings.filter((saving) => saving.id === pk);
};

const depositsInfo = function (pk) {
  return destore.deposits.filter((deposit) => deposit.id === pk);
};

const ProfileEdit = () => {
  router.push("/profileEdit");
};

const recommendDeposits = ref([]);
const recommendSavings = ref([]);

const exit = function () {
  console.log(userstore.API_URL);
  axios({
    method: "delete",
    url: `${userstore.API_URL}/accounts/update/`,
    headers: {
      Authorization: `Token ${userstore.loginUser.token}`,
    },
  });
  alert("다시 돌아오실 날을 기다릴게요...🥺");
  userstore.loginUser = {
    age: 0,
    email: "",
    first_name: "",
    gender: "Female",
    income: 0,
    job: "",
    last_name: "",
    nickname: "",
    pk: 0,
    username: "",
    token: "",
    deposits: [],
    savings: [],
  };
  router.push({ name: "home" });
};

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/accounts/recommend/`,
    headers: {
      Authorization: `Token ${userstore.loginUser.token}`,
    },
  })
    .then((response) => {
      recommendDeposits.value = response.data.deposit;
      recommendSavings.value = response.data.saving;
    })
    .catch((error) => {
      console.log(error);
    });
});
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
