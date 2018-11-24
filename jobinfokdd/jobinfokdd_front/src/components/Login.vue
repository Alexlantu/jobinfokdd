<template>
    <div class="login">
        <form method="post" action="">
            <h1>{{ msg }}</h1>
            <label>登陆</label><br>
            <label>账号</label>
            <input type="text" name="uid"><br>
            <label>密码</label>
            <input type="password" name="upwd"><br>
            <button type="submit">注册</button>
            <button type="submit">登陆</button>
      </form>
    </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      msg: '这是修改后的页面'
    }
  }
}
</script>

<style>

</style>
