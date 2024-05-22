<template>
  <section class="bg-white">
    <div class="lg:grid lg:min-h-screen lg:grid-cols-12">
      <section
        class="relative flex h-32 items-end bg-gray-900 lg:col-span-5 lg:h-full xl:col-span-6"
      >
        <img
          alt=""
          src="@/assets/bgc.png"
          class="absolute inset-0 h-full w-full object-cover opacity-80"
        />

        <div class="hidden lg:relative lg:block lg:p-12">
          <a><img src="@/assets/zz.png" alt="" /> </a>

          <h2
            class="mt-6 text-2xl font-bold text-white sm:text-3xl md:text-4xl"
          >
            회원가입 지전 따봉
          </h2>

          <p class="mt-4 leading-relaxed text-white/90">힘들다</p>
        </div>
      </section>

      <main
        class="flex items-center justify-center px-8 py-8 sm:px-12 lg:col-span-7 lg:px-16 lg:py-12 xl:col-span-6"
      >
        <div class="max-w-xl lg:max-w-3xl">
          <form @submit.prevent="signUp" class="mt-8 grid grid-cols-6 gap-6">
            <div class="col-span-6 sm:col-span-3">
              <label
                for="username"
                class="block text-sm font-medium text-gray-700"
              >
                아이디
              </label>

              <input
                type="text"
                id="username"
                v-model.trim="username"
                class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
              />
            </div>

            <div class="col-span-6 sm:col-span-3">
              <label
                for="nickname"
                class="block text-sm font-medium text-gray-700"
              >
                닉네임
              </label>

              <input
                type="text"
                id="nickname"
                v-model.trim="nickname"
                class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
              />
            </div>
            <div class="col-span-6 sm:col-span-3">
              <label
                for="email"
                class="block text-sm font-medium text-gray-700"
              >
                이메일
              </label>

              <input
                type="email"
                id="email"
                v-model.trim="email"
                class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
              />
            </div>

            <div class="col-span-6 sm:col-span-3">
              <label
                for="password1"
                class="block text-sm font-medium text-gray-700"
              >
                비밀번호
              </label>

              <input
                type="password"
                id="password1"
                v-model.trim="password1"
                class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
              />
            </div>

            <div class="col-span-6 sm:col-span-3">
              <label
                for="password2"
                class="block text-sm font-medium text-gray-700"
              >
                비밀번호 확인
              </label>

              <input
                type="password"
                id="password2"
                v-model.trim="password2"
                class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
              />
            </div>

            <div class="flex">
              <label for="성별"></label>
              <div class="flex items-center me-4">
                <input
                  id="Male"
                  type="radio"
                  value="Male"
                  name="Male"
                  v-model="gender"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                />
                <label
                  for="Male"
                  class="ms-4 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >남성</label
                >
              </div>
              <div class="flex items-center me-4">
                <input
                  id="Female"
                  type="radio"
                  value="Female"
                  name="Female"
                  v-model="gender"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                />
                <label
                  for="Female"
                  class="ms-4 text-sm font-medium text-gray-900 dark:text-gray-300"
                  >여성</label
                >
              </div>
            </div>

            <div class="col-span-6 sm:col-span-3">
              <label for="age" class="block text-sm font-medium text-gray-700">
                나이
              </label>

              <input
                type="text"
                id="age"
                v-model.trim="age"
                class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
              />
            </div>

            <div class="col-span-6 sm:col-span-3">
              <label
                for="income"
                class="block text-sm font-medium text-gray-700"
              >
                연봉(천원단위)
              </label>

              <input
                type="text"
                id="income"
                v-model.trim="income"
                class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
              />
            </div>

            <div class="col-span-6 sm:col-span-3">
              <label
                for="job"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >직업</label
              >
              <select
                id="job"
                v-model="job"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              >
                <option value="Analyst">어널리스트</option>
                <option value="Teacher">센세</option>
                <option value="Lawyer">변호사</option>
                <option value="Researcher">조사하는사람</option>
                <option value="Photographer">사진작가</option>
                <option value="Manager">마네쟈</option>
                <option value="Writer">작가</option>
                <option value="Designer">디자이너</option>
                <option value="Doctor">의사</option>
                <option value="Artist">예술가</option>
                <option value="Nurse">간호사</option>
                <option value="Chef">요리사</option>
                <option value="Student">학생</option>
                <option value="Engineer">엔지니어</option>
                <option value="Marketer">마케터</option>
                <option value="Developer">Developer</option>
                <option value="Accountant">회계사</option>
              </select>
            </div>

            <div class="col-span-6">
              <label for="MarketingAccept" class="flex gap-4">
                <input
                  type="checkbox"
                  id="MarketingAccept"
                  name="marketing_accept"
                  class="size-5 rounded-md border-gray-200 bg-white shadow-sm"
                />

                <span class="text-sm text-gray-700">
                  이벤트성 정보 수신에 동의합니다 (동작안함)
                </span>
              </label>
            </div>

            <div class="col-span-6">
              <p class="text-sm text-gray-500">
                개인정보처리약관이랑
                <a href="#" class="text-gray-700 underline"> 기타등등이랑 </a>
                다
                <a href="#" class="text-gray-700 underline"
                  >동의하시죠? (동작안함)</a
                >.
              </p>
            </div>

            <div class="col-span-6 sm:flex sm:items-center sm:gap-4">
              <input
                type="submit"
                value="계정 생성하기"
                class="inline-block shrink-0 rounded-md border border-blue-600 bg-blue-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-transparent hover:text-blue-600 focus:outline-none focus:ring active:text-blue-500"
              />

              <p class="mt-4 text-sm text-gray-500 sm:mt-0">
                이미 계정이 있으신가요?
                <a href="#" class="text-gray-700 underline">로그인 페이지로</a>.
              </p>
            </div>
          </form>
        </div>
      </main>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const store = useUserStore();
const router = useRouter();

const username = ref("");
const password1 = ref("");
const password2 = ref("");
const email = ref("");
const age = ref("");
const nickname = ref("");
const job = ref(null);
const income = ref("");
const gender = ref(null);

const signUp = () => {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    age: age.value,
    job: job.value,
    nickname: nickname.value,
    income: income.value,
    gender: gender.value,
  };

  store
    .signUp(payload)
    .then(() => {
      router.push({ name: "home" }); // 회원가입 성공 후 홈으로 이동
    })
    .catch((err) => {
      console.error("회원가입 실패:", err);
    });
};
</script>

<style scoped>
/* 스타일 추가 */
</style>
