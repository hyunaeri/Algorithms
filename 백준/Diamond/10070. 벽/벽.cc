#include<cstdio>
#include<algorithm>
using namespace std;
const int MXN = 2e6, inf = 1e5;
int n, k;
struct st {
    int low, up;
    st operator+(st i) {
        return{ min(max(low,i.low),i.up),min(max(up,i.low),i.up) };
    }
}tree[MXN * 4];
void update(int h, int l, int r, int gl, int gr, st x) {
    if (r < gl || gr < l) return;
    if (l^r) {
        tree[h * 2 + 1] = tree[h * 2 + 1] + tree[h];
        tree[h * 2 + 2] = tree[h * 2 + 2] + tree[h];
        tree[h] = { 0,inf };
    }
    if (gl <= l&&r <= gr) tree[h] = tree[h] + x;
    else {
        update(h * 2 + 1, l, (l + r) / 2, gl, gr, x);
        update(h * 2 + 2, (l + r) / 2 + 1, r, gl, gr, x);
    }
}
st query(int h, int l, int r, int g) {
    if (r < g || g < l) return{ 0,inf };
    if (l == r) return tree[h];
    return query(h * 2 + 1, l, (l + r) / 2, g) + query(h * 2 + 2, (l + r) / 2 + 1, r, g) + tree[h];
}
int main() {
    for (scanf("%d%d", &n, &k); k--;) {
        int op, l, r, h;
        scanf("%d%d%d%d", &op, &l, &r, &h);
        if (op == 1) update(0, 0, n - 1, l, r, { h, inf });
        else update(0, 0, n - 1, l, r, { 0,h });
    }
    for (int i = 0; i < n; i++) printf("%d\n", query(0, 0, n - 1, i).up);
    return 0;
}