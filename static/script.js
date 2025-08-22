document.getElementById('groupForm').addEventListener('submit', function(e) {
    const names = document.getElementById('names').value;
    const numGroups = document.getElementById('num_groups').value;
    
    if (!names.trim()) {
        e.preventDefault();
        alert('請輸入至少一個名字！');
        return;
    }
    
    if (numGroups < 1) {
        e.preventDefault();
        alert('分組數量必須大於0！');
        return;
    }
});