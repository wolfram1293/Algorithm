function calculate() {
    let A = document.getElementById('Avalue')
    let B = document.getElementById('Bvalue')
    var time = Math.round((Number(A.value) * 60 + Number(B.value)) * 42.195)
    var s = time % 60
    time = (time - s) / 60
    var m = time % 60
    time = (time - m) / 60
    var h = time % 60
    document.getElementById('ans').innerHTML = h + '時間' + m + '分' + s + '秒'
}