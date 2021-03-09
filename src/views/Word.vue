<template>
  <div>
    <el-container>
      <el-header>
        <h1>好的 (1/10)</h1>
      </el-header>
      <el-main>
        <div>
          <el-input v-model="input" placeholder="请输入对应单词" style="width: 200px"></el-input>
        </div>
        <!-- 输入完成 -->
        <div style="margin: 100px;"></div>
        <el-button type="success" round @click="verification">确认</el-button>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Word",
  props: {
    image: {
      type: String,
      
    },
    zIndex: {
      type: Number,
      default: 1
    },
    width: {
      type: String,
      default: '150px'
    },
    height: {
      type: String,
      default: '150px'
    }
  },
  data() {
    return {
      input: ''
    }
  },
  
  methods: {
    // 单词校验
    verification:function() {
      if (this.input === 'ok') {
        this.$message({
          message: '恭喜你，答对了！',
          type: 'success'
        })
        setInterval(() => {
          this.next()
        }, 1000);
        
      } else {
        this.$message({
          message: '错了哦，再想想！',
          type: 'error'
        });
      }
    },
    // 下一步
    next() {
      this.input = ''
      console.log('next')
    }
  }
};
</script>

<style scoped>
</style>
