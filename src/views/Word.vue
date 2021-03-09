<template>
  <div>
    <el-container>
      <el-header>
        <h1>
          {{ currentWord.chinese }} ({{ wordsLengh - words.length }}/{{
            wordsLengh
          }})
        </h1>
      </el-header>
      <el-main>
        <div>
          <el-input
            v-model="inputWord"
            placeholder="请输入对应单词"
            style="width: 200px"
          ></el-input>
        </div>

        <!-- 输入完成 -->
        <el-button
          v-if="gameOver === false"
          style="margin: 100px"
          type="success"
          round
          @click="verification"
          >确认</el-button
        >
        <el-button
          v-if="gameOver === true"
          style="margin: 100px"
          type="success"
          round
          @click="backHome"
          >结束</el-button
        >
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Word",
  data() {
    return {
      inputWord: "",
      wordsLengh: 0,
      words: [],
      currentWord: {},
      gameOver: false,
    };
  },
  created() {
    this.words = JSON.parse(JSON.stringify(this.$route.params.words));
    this.wordsLengh = this.words.length;
    const randomIndex = Math.floor(Math.random() * this.words.length); // 可均衡获取 0 到 length 的随机整数。
    this.currentWord = this.words[randomIndex];
    this.words.splice(randomIndex, 1);
  },
  methods: {
    // 单词校验
    verification: function () {
      if (this.inputWord.toLowerCase() === this.currentWord.english.toLowerCase()) {
        this.$message({
          message: "恭喜你，答对了！",
          type: "success",
        });
        // 进入下一个单词
        setTimeout(() => {
          this.nextWord();
        }, 1000);
      } else {
        this.$message({
          message: "错了哦，再想想！",
          type: "error",
        });
      }
    },
    // 下一个单词
    nextWord() {
      if (this.words.length > 0) {
        this.inputWord = "";
        const randomIndex = Math.floor(Math.random() * this.words.length); // 可均衡获取 0 到 length 的随机整数。
        this.currentWord = this.words[randomIndex];
        this.words.splice(randomIndex, 1);
      } else {
        this.gameOver = true;
      }
    },
    // 回到首页
    backHome() {
      this.$router.push('/')
    },
  },
};
</script>

<style scoped>
</style>
