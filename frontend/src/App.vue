<script setup>
import { ref } from 'vue'

const activeNav = ref('Dashboard')

const stats = [
  { title: 'Total Revenue', value: '$124,850.00', change: '+12.5%', period: 'vs last month', color: 'bg-blue-500', isUp: true, spark: [10, 15, 8, 12, 18, 14, 20] },
  { title: 'Total Sales', value: '$98,420.00', change: '+8.2%', period: 'vs last month', color: 'bg-emerald-500', isUp: true, spark: [12, 10, 16, 14, 11, 15, 19] },
  { title: 'Total Purchases', value: '$45,230.00', change: '-3.1%', period: 'vs last month', color: 'bg-amber-500', isUp: false, spark: [18, 16, 12, 14, 10, 12, 15] },
  { title: 'Inventory Value', value: '$256,780.00', change: '+6.3%', period: 'vs last month', color: 'bg-purple-500', isUp: true, spark: [10, 12, 15, 11, 18, 16, 21] },
  { title: 'Pending Invoices', value: '28', change: '+5', period: 'vs last month', color: 'bg-rose-500', isUp: false, spark: [5, 8, 12, 10, 15, 14, 18] },
  { title: 'Total Employees', value: '128', change: '+3', period: 'vs last month', color: 'bg-teal-500', isUp: true, spark: [10, 11, 12, 12, 14, 14, 15] }
]

const recentOrders = [
  { id: 'SO-2025-00125', type: 'Sales', entity: 'Acme Corporation', amount: '$12,450.00', status: 'Confirmed', badge: 'bg-emerald-100 text-emerald-700' },
  { id: 'SO-2025-00124', type: 'Sales', entity: 'Globex Industries', amount: '$8,750.00', status: 'Processing', badge: 'bg-blue-100 text-blue-700' },
  { id: 'PO-2025-00098', type: 'Purchase', entity: 'Tech Supplies Ltd.', amount: '$6,230.00', status: 'Approved', badge: 'bg-emerald-100 text-emerald-700' },
  { id: 'PO-2025-00097', type: 'Purchase', entity: 'Global Traders', amount: '$3,840.00', status: 'Received', badge: 'bg-purple-100 text-purple-700' },
  { id: 'SO-2025-000123', type: 'Sales', entity: 'Innotech Solutions', amount: '$15,600.00', status: 'Shipped', badge: 'bg-blue-100 text-blue-700' }
]

const lowStock = [
  { name: 'Wireless Mouse', warehouse: 'Main Warehouse', stock: 5, status: 'Critical', badge: 'bg-rose-100 text-rose-700' },
  { name: 'USB-C Cable', warehouse: 'Main Warehouse', stock: 8, status: 'Critical', badge: 'bg-rose-100 text-rose-700' },
  { name: 'Laptop Stand', warehouse: 'Warehouse B', stock: 12, status: 'Low', badge: 'bg-amber-100 text-amber-700' },
  { name: 'Gaming Keyboard', warehouse: 'Main Warehouse', stock: 15, status: 'Low', badge: 'bg-amber-100 text-amber-700' },
  { name: 'Office Chair', warehouse: 'Warehouse A', stock: 18, status: 'Low', badge: 'bg-amber-100 text-amber-700' }
]

const topSelling = [
  { name: 'Wireless Headphones', sold: 320, revenue: '$15,360.00' },
  { name: 'Smart Watch', sold: 210, revenue: '$12,600.00' },
  { name: 'Bluetooth Speaker', sold: 185, revenue: '$9,250.00' },
  { name: 'Laptop Backpack', sold: 160, revenue: '$8,320.00' },
  { name: 'Wireless Mouse', sold: 145, revenue: '$7,250.00' }
]

const notifications = [
  { title: 'Low stock alert for Wireless Mouse', desc: 'Stock remaining: 5 units', time: '10 min ago', color: 'bg-rose-500' },
  { title: 'Invoice INV-2025-00045 is overdue', desc: 'Amount: $2,450.00', time: '1 hour ago', color: 'bg-blue-500' },
  { title: 'Leave request approved', desc: 'John Doe - 3 days', time: '2 hours ago', color: 'bg-emerald-500' },
  { title: 'New purchase order PO-2025-00098 created', desc: 'Supplier: Tech Supplies Ltd.', time: '3 hours ago', color: 'bg-purple-500' }
]
</script>

<template>
  <div class="flex h-screen bg-[#f4f6f9] text-slate-800 text-xs font-sans overflow-hidden">
    <!-- Dark Sidebar -->
    <aside class="w-60 bg-[#0f172a] text-slate-300 flex flex-col justify-between shrink-0">
      <div>
        <!-- Logo Header -->
        <div class="p-4 flex items-center gap-3 border-b border-slate-800">
          <div class="w-8 h-8 rounded-lg bg-blue-600 flex items-center justify-center font-bold text-white text-sm">E</div>
          <div>
            <h2 class="font-bold text-white text-sm leading-tight">Distributed ERP</h2>
            <p class="text-[10px] text-slate-400">Enterprise Management System</p>
          </div>
        </div>

        <!-- Navigation Menu -->
        <div class="p-3 space-y-4 overflow-y-auto max-h-[calc(100vh-140px)]">
          <div>
            <button @click="activeNav = 'Dashboard'" :class="activeNav === 'Dashboard' ? 'bg-blue-600 text-white' : 'hover:bg-slate-800 text-slate-400'" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-left font-medium">
              <span>📊</span> Dashboard
            </button>
          </div>

          <div>
            <p class="px-3 text-[10px] uppercase tracking-wider text-slate-500 font-semibold mb-1">Core Modules</p>
            <div class="space-y-0.5">
              <button v-for="item in ['Employees', 'Attendance', 'Leaves']" :key="item" class="w-full flex items-center gap-3 px-3 py-1.5 rounded-md hover:bg-slate-800 text-slate-400 text-left">
                <span>👤</span> {{ item }}
              </button>
            </div>
          </div>

          <div>
            <p class="px-3 text-[10px] uppercase tracking-wider text-slate-500 font-semibold mb-1">Inventory</p>
            <div class="space-y-0.5">
              <button v-for="item in ['Products', 'Warehouses', 'Stock Movements', 'Suppliers']" :key="item" class="w-full flex items-center gap-3 px-3 py-1.5 rounded-md hover:bg-slate-800 text-slate-400 text-left">
                <span>📦</span> {{ item }}
              </button>
            </div>
          </div>

          <div>
            <p class="px-3 text-[10px] uppercase tracking-wider text-slate-500 font-semibold mb-1">Purchase</p>
            <div class="space-y-0.5">
              <button v-for="item in ['Purchase Orders', 'Goods Received', 'Purchase Returns']" :key="item" class="w-full flex items-center gap-3 px-3 py-1.5 rounded-md hover:bg-slate-800 text-slate-400 text-left">
                <span>🛍️</span> {{ item }}
              </button>
            </div>
          </div>

          <div>
            <p class="px-3 text-[10px] uppercase tracking-wider text-slate-500 font-semibold mb-1">Sales</p>
            <div class="space-y-0.5">
              <button v-for="item in ['Customers', 'Sales Orders', 'Returns']" :key="item" class="w-full flex items-center gap-3 px-3 py-1.5 rounded-md hover:bg-slate-800 text-slate-400 text-left">
                <span>💼</span> {{ item }}
              </button>
            </div>
          </div>

          <div>
            <p class="px-3 text-[10px] uppercase tracking-wider text-slate-500 font-semibold mb-1">Billing</p>
            <div class="space-y-0.5">
              <button v-for="item in ['Invoices', 'Payments']" :key="item" class="w-full flex items-center gap-3 px-3 py-1.5 rounded-md hover:bg-slate-800 text-slate-400 text-left">
                <span>💳</span> {{ item }}
              </button>
            </div>
          </div>

          <div>
            <p class="px-3 text-[10px] uppercase tracking-wider text-slate-500 font-semibold mb-1">Other</p>
            <div class="space-y-0.5">
              <button class="w-full flex items-center justify-between px-3 py-1.5 rounded-md hover:bg-slate-800 text-slate-400">
                <span class="flex items-center gap-3">🔔 Notifications</span>
                <span class="bg-rose-500 text-white text-[10px] px-1.5 py-0.2 rounded-full">12</span>
              </button>
              <button v-for="item in ['Reports', 'Audit Logs', 'Settings']" :key="item" class="w-full flex items-center gap-3 px-3 py-1.5 rounded-md hover:bg-slate-800 text-slate-400 text-left">
                <span>⚙️</span> {{ item }}
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- User Info Footer -->
      <div class="p-3 bg-slate-900 border-t border-slate-800 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div class="w-7 h-7 rounded-full bg-emerald-600 flex items-center justify-center font-bold text-white">JD</div>
          <div>
            <p class="font-semibold text-white leading-tight">John Doe</p>
            <p class="text-[9px] text-emerald-400">ADMIN ●</p>
          </div>
        </div>
        <button class="text-slate-500 hover:text-white">◀</button>
      </div>
    </aside>

    <!-- Main Content -->
    <div class="flex-1 flex flex-col overflow-y-auto">
      <!-- Top Header Navigation Bar -->
      <header class="h-12 bg-white border-b border-slate-200 flex items-center justify-between px-4 shrink-0">
        <div class="flex items-center gap-3 w-1/3">
          <button class="text-slate-500">☰</button>
          <div class="relative w-full">
            <input type="text" placeholder="Search anything... (Ctrl + K)" class="w-full bg-slate-100 text-xs py-1 px-3 rounded-md border border-slate-200 focus:outline-none" />
          </div>
        </div>

        <div class="flex items-center gap-4">
          <button class="text-slate-500">🌙</button>
          <div class="relative">
            <button class="text-slate-500">🔔</button>
            <span class="absolute -top-1 -right-1 bg-rose-500 text-white text-[9px] px-1 rounded-full">12</span>
          </div>
          <button class="text-slate-500">⛶</button>
          <div class="flex items-center gap-2 border-l pl-3 border-slate-200">
            <div class="text-right">
              <p class="font-semibold leading-tight">John Doe</p>
              <p class="text-[10px] text-slate-400">ADMIN</p>
            </div>
            <div class="w-7 h-7 rounded-full bg-slate-300 flex items-center justify-center font-bold text-slate-600">JD</div>
          </div>
        </div>
      </header>

      <!-- Dashboard View Content -->
      <main class="p-5 space-y-5">
        <!-- Title & Date Selector -->
        <div class="flex items-center justify-between">
          <div>
            <h1 class="text-lg font-bold text-slate-800">Dashboard</h1>
            <p class="text-[11px] text-slate-400">Home &gt; <span class="text-blue-600">Dashboard</span></p>
          </div>
          <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-md px-3 py-1 shadow-xs">
            <span>📅</span>
            <span class="text-slate-600 font-medium">May 15, 2025 - Jun 15, 2025</span>
          </div>
        </div>

        <!-- 6 Metrics Top Row -->
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-3">
          <div v-for="stat in stats" :key="stat.title" class="bg-white p-3 rounded-xl border border-slate-100 shadow-xs flex flex-col justify-between">
            <div>
              <div class="flex items-center gap-2 mb-2">
                <div :class="[stat.color, 'w-6 h-6 rounded-md flex items-center justify-center text-white text-[10px]']">📊</div>
                <span class="text-[11px] text-slate-500 font-medium">{{ stat.title }}</span>
              </div>
              <p class="text-base font-bold text-slate-800">{{ stat.value }}</p>
              <div class="flex items-center gap-1 mt-1">
                <span :class="stat.isUp ? 'text-emerald-600' : 'text-rose-600'" class="font-bold text-[10px]">{{ stat.change }}</span>
                <span class="text-[10px] text-slate-400">{{ stat.period }}</span>
              </div>
            </div>
            <!-- Mini Sparkline Placeholder -->
            <div class="h-6 mt-2 flex items-end gap-1 opacity-60">
              <div v-for="(v, i) in stat.spark" :key="i" :style="{ height: v * 2 + 'px' }" class="flex-1 bg-blue-500 rounded-t-xs"></div>
            </div>
          </div>
        </div>

        <!-- Revenue Overview & Recent Orders Row -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
          <!-- Revenue Overview Card -->
          <div class="lg:col-span-6 bg-white p-4 rounded-xl border border-slate-100 shadow-xs">
            <div class="flex items-center justify-between mb-4">
              <h2 class="font-bold text-slate-800">Revenue Overview</h2>
              <select class="bg-slate-50 border border-slate-200 rounded px-2 py-0.5 text-xs text-slate-600">
                <option>This Month</option>
              </select>
            </div>
            <div class="flex items-center gap-4 text-[11px] mb-2">
              <span class="flex items-center gap-1 text-blue-600 font-medium"><span class="w-2 h-2 rounded-full bg-blue-600"></span> Revenue</span>
              <span class="flex items-center gap-1 text-rose-500 font-medium"><span class="w-2 h-2 rounded-full bg-rose-500"></span> Expenses</span>
            </div>
            <!-- Chart Area Container -->
            <div class="h-44 border-b border-l border-slate-200 flex items-end justify-between px-4 pb-2 relative bg-gradient-to-t from-blue-50/50 to-transparent rounded-b-md">
              <span class="text-[9px] text-slate-400 absolute left-1 top-2">$25K</span>
              <span class="text-[9px] text-slate-400 absolute left-1 top-1/2">$15K</span>
              <span class="text-[9px] text-slate-400 absolute left-1 bottom-2">$0</span>
              <div v-for="day in ['May 15', 'May 22', 'May 29', 'Jun 05', 'Jun 12']" :key="day" class="text-[10px] text-slate-400">{{ day }}</div>
            </div>
          </div>

          <!-- Recent Orders Card -->
          <div class="lg:col-span-6 bg-white p-4 rounded-xl border border-slate-100 shadow-xs">
            <div class="flex items-center justify-between mb-3">
              <h2 class="font-bold text-slate-800">Recent Orders</h2>
              <a href="#" class="text-blue-600 text-[11px] font-medium">View All</a>
            </div>
            <div class="overflow-x-auto">
              <table class="w-full text-left">
                <thead>
                  <tr class="text-slate-400 border-b border-slate-100 text-[10px]">
                    <th class="pb-2">Order ID</th>
                    <th class="pb-2">Type</th>
                    <th class="pb-2">Customer/Supplier</th>
                    <th class="pb-2">Amount</th>
                    <th class="pb-2 text-right">Status</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-50 text-[11px]">
                  <tr v-for="order in recentOrders" :key="order.id" class="hover:bg-slate-50">
                    <td class="py-2 text-blue-600 font-medium">{{ order.id }}</td>
                    <td class="py-2 text-slate-500">{{ order.type }}</td>
                    <td class="py-2 font-medium">{{ order.entity }}</td>
                    <td class="py-2 font-mono">{{ order.amount }}</td>
                    <td class="py-2 text-right">
                      <span :class="[order.badge, 'px-2 py-0.5 rounded-full font-medium text-[10px]']">{{ order.status }}</span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- Bottom Grid (Low Stock, Top Selling, Notifications) -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
          <!-- Low Stock Products -->
          <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-xs">
            <div class="flex items-center justify-between mb-3">
              <h2 class="font-bold text-slate-800">Low Stock Products</h2>
              <a href="#" class="text-blue-600 text-[11px] font-medium">View All</a>
            </div>
            <div class="space-y-2">
              <div v-for="item in lowStock" :key="item.name" class="flex items-center justify-between p-1.5 hover:bg-slate-50 rounded-lg">
                <div class="flex items-center gap-2">
                  <div class="w-6 h-6 rounded bg-slate-100 flex items-center justify-center text-slate-500">📦</div>
                  <div>
                    <p class="font-semibold text-slate-800">{{ item.name }}</p>
                    <p class="text-[10px] text-slate-400">{{ item.warehouse }}</p>
                  </div>
                </div>
                <div class="flex items-center gap-3">
                  <span class="font-mono text-slate-600 font-semibold">{{ item.stock }}</span>
                  <span :class="[item.badge, 'px-2 py-0.5 rounded text-[10px] font-medium']">{{ item.status }}</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Top Selling Products -->
          <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-xs">
            <div class="flex items-center justify-between mb-3">
              <h2 class="font-bold text-slate-800">Top Selling Products</h2>
              <a href="#" class="text-blue-600 text-[11px] font-medium">View All</a>
            </div>
            <div class="space-y-2">
              <div v-for="item in topSelling" :key="item.name" class="flex items-center justify-between p-1.5 hover:bg-slate-50 rounded-lg">
                <div class="flex items-center gap-2">
                  <div class="w-6 h-6 rounded bg-slate-100 flex items-center justify-center text-slate-500">🎧</div>
                  <div>
                    <p class="font-semibold text-slate-800">{{ item.name }}</p>
                    <p class="text-[10px] text-slate-400">{{ item.sold }} Sold</p>
                  </div>
                </div>
                <span class="font-mono text-slate-700 font-bold">{{ item.revenue }}</span>
              </div>
            </div>
          </div>

          <!-- Notifications -->
          <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-xs">
            <div class="flex items-center justify-between mb-3">
              <h2 class="font-bold text-slate-800">Notifications</h2>
              <a href="#" class="text-blue-600 text-[11px] font-medium">View All</a>
            </div>
            <div class="space-y-3">
              <div v-for="notif in notifications" :key="notif.title" class="flex items-start gap-3 p-1">
                <div :class="[notif.color, 'w-6 h-6 rounded-full flex items-center justify-center text-white shrink-0 mt-0.5 text-[10px]']">🔔</div>
                <div class="flex-1">
                  <p class="font-semibold text-slate-800 leading-tight">{{ notif.title }}</p>
                  <p class="text-[10px] text-slate-400 mt-0.5">{{ notif.desc }}</p>
                </div>
                <span class="text-[9px] text-slate-400 shrink-0">{{ notif.time }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Footer -->
        <footer class="flex items-center justify-between pt-4 text-[10px] text-slate-400 border-t border-slate-200">
          <p>© 2025 Distributed ERP. All rights reserved.</p>
          <p>Version 1.0.0</p>
        </footer>
      </main>
    </div>
  </div>
</template>