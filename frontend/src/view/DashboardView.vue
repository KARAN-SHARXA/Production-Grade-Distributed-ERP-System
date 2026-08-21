<script setup>
import { ref } from 'vue'

// --- MOCK METRIC CARDS ---
const metrics = ref([
  {
    title: 'Total Revenue',
    value: '$124,850.00',
    change: '+12.5%',
    isPositive: true,
    bgIcon: 'bg-blue-500',
    iconColor: 'text-blue-500',
    sparklineBg: 'bg-blue-50',
    svgColor: '#3B82F6',
    icon: 'M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z'
  },
  {
    title: 'Total Sales',
    value: '$98,420.00',
    change: '+8.2%',
    isPositive: true,
    bgIcon: 'bg-emerald-500',
    iconColor: 'text-emerald-500',
    sparklineBg: 'bg-emerald-50',
    svgColor: '#10B981',
    icon: 'M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z'
  },
  {
    title: 'Total Purchases',
    value: '$45,230.00',
    change: '-3.1%',
    isPositive: false,
    bgIcon: 'bg-amber-500',
    iconColor: 'text-amber-500',
    sparklineBg: 'bg-amber-50',
    svgColor: '#F59E0B',
    icon: 'M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z'
  },
  {
    title: 'Inventory Value',
    value: '$256,780.00',
    change: '+6.3%',
    isPositive: true,
    bgIcon: 'bg-indigo-500',
    iconColor: 'text-indigo-500',
    sparklineBg: 'bg-indigo-50',
    svgColor: '#6366F1',
    icon: 'M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4'
  },
  {
    title: 'Pending Invoices',
    value: '28',
    change: '+5',
    isPositive: false, // Highlighted red for action needed
    bgIcon: 'bg-rose-500',
    iconColor: 'text-rose-500',
    sparklineBg: 'bg-rose-50',
    svgColor: '#F43F5E',
    icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z'
  },
  {
    title: 'Total Employees',
    value: '128',
    change: '+3',
    isPositive: true,
    bgIcon: 'bg-teal-500',
    iconColor: 'text-teal-500',
    sparklineBg: 'bg-teal-50',
    svgColor: '#14B8A6',
    icon: 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5 5 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z'
  }
])

// --- MOCK TABLES & DATA LISTS ---
const recentOrders = ref([
  { id: 'SO-2025-00125', type: 'Sales', entity: 'Acme Corporation', amount: '$12,450.00', status: 'Confirmed', statusStyle: 'bg-emerald-50 text-emerald-600 border-emerald-200' },
  { id: 'SO-2025-00124', type: 'Sales', entity: 'Globex Industries', amount: '$8,750.00', status: 'Processing', statusStyle: 'bg-blue-50 text-blue-600 border-blue-200' },
  { id: 'PO-2025-00098', type: 'Purchase', entity: 'Tech Supplies Ltd.', amount: '$6,230.00', status: 'Approved', statusStyle: 'bg-emerald-50 text-emerald-600 border-emerald-200' },
  { id: 'PO-2025-00097', type: 'Purchase', entity: 'Global Traders', amount: '$3,840.00', status: 'Received', statusStyle: 'bg-purple-50 text-purple-600 border-purple-200' },
  { id: 'SO-2025-00123', type: 'Sales', entity: 'Innotech Solutions', amount: '$15,600.00', status: 'Shipped', statusStyle: 'bg-sky-50 text-sky-600 border-sky-200' }
])

const lowStockProducts = ref([
  { name: 'Wireless Mouse', warehouse: 'Main Warehouse', stock: 5, status: 'Critical', style: 'bg-rose-50 text-rose-600' },
  { name: 'USB-C Cable', warehouse: 'Main Warehouse', stock: 8, status: 'Critical', style: 'bg-rose-50 text-rose-600' },
  { name: 'Laptop Stand', warehouse: 'Warehouse B', stock: 12, status: 'Low', style: 'bg-amber-50 text-amber-600' },
  { name: 'Gaming Keyboard', warehouse: 'Main Warehouse', stock: 15, status: 'Low', style: 'bg-amber-50 text-amber-600' },
  { name: 'Office Chair', warehouse: 'Warehouse A', stock: 18, status: 'Low', style: 'bg-amber-50 text-amber-600' }
])

const topProducts = ref([
  { name: 'Wireless Headphones', sold: 320, revenue: '$15,360.00' },
  { name: 'Smart Watch', sold: 210, revenue: '$12,600.00' },
  { name: 'Bluetooth Speaker', sold: 185, revenue: '$9,250.00' },
  { name: 'Laptop Backpack', sold: 160, revenue: '$8,320.00' },
  { name: 'Wireless Mouse', sold: 145, revenue: '$7,250.00' }
])

const notifications = ref([
  { id: 1, title: 'Low stock alert for Wireless Mouse', desc: 'Stock remaining: 5 units', time: '10 min ago', color: 'bg-rose-500', icon: 'M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z' },
  { id: 2, title: 'Invoice INV-2025-00045 is overdue', desc: 'Amount: $2,450.00', time: '1 hour ago', color: 'bg-blue-500', icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z' },
  { id: 3, title: 'Leave request approved', desc: 'John Doe - 3 days', time: '2 hours ago', color: 'bg-emerald-500', icon: 'M5 13l4 4L19 7' },
  { id: 4, title: 'New purchase order PO-2025-00098 created', desc: 'Supplier: Tech Supplies Ltd.', time: '3 hours ago', color: 'bg-indigo-500', icon: 'M3 3h2l.4 2M7 13h10l4-8H5.4' }
])
</script>

<template>
  <div class="flex h-screen bg-[#F4F6F9] font-sans antialiased text-slate-800 overflow-hidden">
    <!-- ================= SIDEBAR ================= -->
    <aside class="w-64 bg-[#0B132B] text-slate-300 flex flex-col justify-between shrink-0 select-none">
      <div>
        <!-- Logo -->
        <div class="flex items-center gap-3 px-6 py-5 border-b border-slate-800">
          <div class="h-9 w-9 rounded-xl bg-blue-600 flex items-center justify-center font-bold text-white text-lg shadow-md shadow-blue-500/30">
            Σ
          </div>
          <div>
            <h1 class="font-bold text-white text-base tracking-wide leading-none">Distributed ERP</h1>
            <span class="text-[11px] text-slate-400">Enterprise Management System</span>
          </div>
        </div>

        <!-- Navigation Sections -->
        <nav class="px-3 py-4 space-y-6 overflow-y-auto max-h-[calc(100vh-140px)] text-xs">
          <!-- Main Menu -->
          <div>
            <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-blue-600 text-white font-medium shadow-sm transition">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
              Dashboard
            </a>
          </div>

          <!-- CORE MODULES -->
          <div>
            <p class="px-3 text-[10px] font-semibold text-slate-500 uppercase tracking-wider mb-2">Core Modules</p>
            <div class="space-y-1">
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>Employees</a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>Attendance</a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/></svg>Leaves</a>
            </div>
          </div>

          <!-- INVENTORY -->
          <div>
            <p class="px-3 text-[10px] font-semibold text-slate-500 uppercase tracking-wider mb-2">Inventory</p>
            <div class="space-y-1">
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>Products</a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1"/></svg>Warehouses</a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/></svg>Stock Movements</a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5 5 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>Suppliers</a>
            </div>
          </div>

          <!-- PURCHASE -->
          <div>
            <p class="px-3 text-[10px] font-semibold text-slate-500 uppercase tracking-wider mb-2">Purchase</p>
            <div class="space-y-1">
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>Purchase Orders</a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>Goods Received</a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6"/></svg>Purchase Returns</a>
            </div>
          </div>

          <!-- SALES -->
          <div>
            <p class="px-3 text-[10px] font-semibold text-slate-500 uppercase tracking-wider mb-2">Sales</p>
            <div class="space-y-1">
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5 5 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>Customers</a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z"/></svg>Sales Orders</a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6"/></svg>Returns</a>
            </div>
          </div>

          <!-- OTHER -->
          <div>
            <p class="px-3 text-[10px] font-semibold text-slate-500 uppercase tracking-wider mb-2">Other</p>
            <div class="space-y-1">
              <a href="#" class="flex items-center justify-between px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition">
                <span class="flex items-center gap-3"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/></svg>Notifications</span>
                <span class="px-1.5 py-0.5 text-[10px] font-bold rounded-full bg-rose-500 text-white">12</span>
              </a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 012-2h2a2 2 0 012 2v6a2 2 0 01-2 2h-2a2 2 0 01-2-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>Reports</a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>Audit Logs</a>
              <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800/60 hover:text-white transition"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/></svg>Settings</a>
            </div>
          </div>
        </nav>
      </div>

      <!-- User Profile Bottom Widget -->
      <div class="p-4 border-t border-slate-800 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="relative">
            <img class="w-9 h-9 rounded-full object-cover border border-slate-700" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=100" alt="John Doe" />
            <span class="absolute bottom-0 right-0 w-2.5 h-2.5 bg-emerald-500 border-2 border-[#0B132B] rounded-full"></span>
          </div>
          <div>
            <p class="text-xs font-semibold text-white leading-tight">John Doe</p>
            <p class="text-[10px] text-slate-400">ADMIN</p>
          </div>
        </div>
        <button class="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
        </button>
      </div>
    </aside>

    <!-- ================= MAIN CONTENT AREA ================= -->
    <div class="flex-1 flex flex-col min-w-0 overflow-y-auto">
      <!-- TOP NAVBAR -->
      <header class="bg-white border-b border-slate-200 sticky top-0 z-10 flex items-center justify-between px-8 py-3.5 shadow-xs">
        <!-- Search bar -->
        <div class="flex items-center gap-4 w-96">
          <button class="text-slate-400 hover:text-slate-600"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"/></svg></button>
          <div class="relative w-full">
            <input type="text" placeholder="Search anything...          Ctrl + K" class="w-full bg-slate-50 border border-slate-200 text-xs text-slate-700 rounded-lg pl-9 pr-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition" />
            <svg class="w-4 h-4 text-slate-400 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          </div>
        </div>

        <!-- Right Quick Actions -->
        <div class="flex items-center gap-5">
          <button class="text-slate-500 hover:text-slate-700"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg></button>
          <div class="relative">
            <button class="text-slate-500 hover:text-slate-700"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/></svg></button>
            <span class="absolute -top-1 -right-1.5 px-1 py-0.2 text-[9px] font-bold rounded-full bg-rose-500 text-white">12</span>
          </div>
          <button class="text-slate-500 hover:text-slate-700"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"/></svg></button>
          
          <div class="h-5 w-px bg-slate-200"></div>

          <div class="flex items-center gap-3">
            <div class="text-right">
              <p class="text-xs font-semibold text-slate-800 leading-none">John Doe</p>
              <p class="text-[10px] text-slate-400 mt-0.5">ADMIN</p>
            </div>
            <img class="w-8 h-8 rounded-full object-cover border border-slate-200" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=100" alt="John Doe" />
          </div>
        </div>
      </header>

      <!-- PAGE CONTENT -->
      <main class="p-8 space-y-6">
        <!-- Header & Date Filter -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold text-slate-900 tracking-tight">Dashboard</h2>
            <p class="text-xs text-slate-500 mt-1">Home &gt; <span class="text-blue-600 font-medium">Dashboard</span></p>
          </div>
          <div class="flex items-center gap-2 bg-white border border-slate-200 rounded-lg px-3 py-1.5 shadow-xs text-xs text-slate-600 font-medium">
            <span>May 15, 2025 - Jun 15, 2025</span>
            <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
          </div>
        </div>

        <!-- 6 TOP METRIC CARDS WITH MINI SPARKLINE CHARTS -->
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-4">
          <div v-for="(item, idx) in metrics" :key="idx" class="bg-white rounded-xl p-4 border border-slate-100 shadow-xs flex flex-col justify-between">
            <div>
              <div class="flex items-center gap-2">
                <div :class="[item.bgIcon, 'p-1.5 rounded-lg text-white']">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="item.icon"/></svg>
                </div>
                <span class="text-[11px] font-medium text-slate-500 truncate">{{ item.title }}</span>
              </div>
              <div class="mt-3">
                <h3 class="text-base font-bold text-slate-900 leading-tight">{{ item.value }}</h3>
                <p class="text-[10px] font-medium mt-0.5" :class="item.isPositive ? 'text-emerald-500' : 'text-rose-500'">
                  {{ item.change }} <span class="text-slate-400 font-normal">vs last month</span>
                </p>
              </div>
            </div>

            <!-- Mini Sparkline Path -->
            <div class="mt-3 pt-2 border-t border-slate-50">
              <svg class="w-full h-8 overflow-visible" viewBox="0 0 100 30" fill="none">
                <path d="M0,25 Q15,5 30,20 T60,10 T90,18 T100,5" fill="none" :stroke="item.svgColor" stroke-width="2" stroke-linecap="round" />
                <circle cx="100" cy="5" r="3" :fill="item.svgColor" />
              </svg>
            </div>
          </div>
        </div>

        <!-- MIDDLE ROW: REVENUE OVERVIEW & RECENT ORDERS -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <!-- Revenue Overview (5 columns) -->
          <div class="lg:col-span-5 bg-white rounded-xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <h3 class="text-sm font-bold text-slate-800">Revenue Overview</h3>
              <select class="text-xs bg-slate-50 border border-slate-200 rounded-lg px-2 py-1 text-slate-600 focus:outline-none">
                <option>This Month</option>
              </select>
            </div>

            <div class="flex items-center gap-6 mt-3 text-xs">
              <span class="flex items-center gap-2 font-medium text-slate-600"><span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span>Revenue</span>
              <span class="flex items-center gap-2 font-medium text-slate-600"><span class="w-2.5 h-2.5 rounded-full bg-rose-400"></span>Expenses</span>
            </div>

            <!-- Mock Chart Graphic -->
            <div class="mt-6 relative h-48 w-full flex items-end">
              <svg class="w-full h-full" viewBox="0 0 300 120" preserveAspectRatio="none">
                <!-- Grid Lines -->
                <line x1="0" y1="30" x2="300" y2="30" stroke="#F1F5F9" stroke-dasharray="4" />
                <line x1="0" y1="60" x2="300" y2="60" stroke="#F1F5F9" stroke-dasharray="4" />
                <line x1="0" y1="90" x2="300" y2="90" stroke="#F1F5F9" stroke-dasharray="4" />

                <!-- Revenue Blue Gradient Area -->
                <path d="M0,80 Q50,50 100,70 T200,40 T300,10 L300,120 L0,120 Z" fill="url(#blueGradient)" opacity="0.15" />
                <path d="M0,80 Q50,50 100,70 T200,40 T300,10" fill="none" stroke="#3B82F6" stroke-width="2.5" />

                <!-- Expenses Rose Line -->
                <path d="M0,100 Q50,80 100,90 T200,70 T300,50" fill="none" stroke="#FB7185" stroke-width="2" stroke-dasharray="3 3" />

                <defs>
                  <linearGradient id="blueGradient" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#3B82F6" />
                    <stop offset="100%" stop-color="#3B82F6" stop-opacity="0" />
                  </linearGradient>
                </defs>
              </svg>
            </div>

            <div class="flex justify-between text-[10px] font-medium text-slate-400 mt-2 px-1">
              <span>May 15</span>
              <span>May 22</span>
              <span>May 29</span>
              <span>Jun 05</span>
              <span>Jun 12</span>
            </div>
          </div>

          <!-- Recent Orders (7 columns) -->
          <div class="lg:col-span-7 bg-white rounded-xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-sm font-bold text-slate-800">Recent Orders</h3>
              <a href="#" class="text-xs font-semibold text-blue-600 hover:underline">View All</a>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead>
                  <tr class="text-slate-400 border-b border-slate-100">
                    <th class="pb-3 font-semibold">Order ID</th>
                    <th class="pb-3 font-semibold">Type</th>
                    <th class="pb-3 font-semibold">Customer/Supplier</th>
                    <th class="pb-3 font-semibold">Amount</th>
                    <th class="pb-3 font-semibold text-right">Status</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-50 text-slate-700">
                  <tr v-for="order in recentOrders" :key="order.id" class="hover:bg-slate-50/80 transition">
                    <td class="py-3 font-medium text-blue-600">{{ order.id }}</td>
                    <td class="py-3 text-slate-500">{{ order.type }}</td>
                    <td class="py-3 font-medium text-slate-800">{{ order.entity }}</td>
                    <td class="py-3 font-semibold text-slate-800">{{ order.amount }}</td>
                    <td class="py-3 text-right">
                      <span :class="['px-2.5 py-1 rounded-full text-[10px] font-semibold border', order.statusStyle]">
                        {{ order.status }}
                      </span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- BOTTOM ROW: THREE WIDGETS -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <!-- Low Stock Products -->
          <div class="bg-white rounded-xl p-5 border border-slate-100 shadow-xs">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-sm font-bold text-slate-800">Low Stock Products</h3>
              <a href="#" class="text-xs font-semibold text-blue-600 hover:underline">View All</a>
            </div>
            <table class="w-full text-left text-xs">
              <thead>
                <tr class="text-slate-400 border-b border-slate-100">
                  <th class="pb-2 font-semibold">Product</th>
                  <th class="pb-2 font-semibold">Warehouse</th>
                  <th class="pb-2 font-semibold">Stock</th>
                  <th class="pb-2 font-semibold text-right">Status</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-50 text-slate-700">
                <tr v-for="(item, i) in lowStockProducts" :key="i">
                  <td class="py-2.5 font-medium text-slate-800 truncate max-w-[100px]">{{ item.name }}</td>
                  <td class="py-2.5 text-slate-400 text-[11px]">{{ item.warehouse }}</td>
                  <td class="py-2.5 font-bold">{{ item.stock }}</td>
                  <td class="py-2.5 text-right">
                    <span :class="['px-2 py-0.5 rounded text-[10px] font-bold', item.style]">{{ item.status }}</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Top Selling Products -->
          <div class="bg-white rounded-xl p-5 border border-slate-100 shadow-xs">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-sm font-bold text-slate-800">Top Selling Products</h3>
              <a href="#" class="text-xs font-semibold text-blue-600 hover:underline">View All</a>
            </div>
            <table class="w-full text-left text-xs">
              <thead>
                <tr class="text-slate-400 border-b border-slate-100">
                  <th class="pb-2 font-semibold">Product</th>
                  <th class="pb-2 font-semibold text-center">Sold</th>
                  <th class="pb-2 font-semibold text-right">Revenue</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-50 text-slate-700">
                <tr v-for="(item, i) in topProducts" :key="i">
                  <td class="py-2.5 font-medium text-slate-800 truncate max-w-[120px]">{{ item.name }}</td>
                  <td class="py-2.5 text-center font-semibold text-slate-600">{{ item.sold }}</td>
                  <td class="py-2.5 text-right font-bold text-slate-800">{{ item.revenue }}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Notifications -->
          <div class="bg-white rounded-xl p-5 border border-slate-100 shadow-xs">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-sm font-bold text-slate-800">Notifications</h3>
              <a href="#" class="text-xs font-semibold text-blue-600 hover:underline">View All</a>
            </div>
            <div class="space-y-3">
              <div v-for="notif in notifications" :key="notif.id" class="flex items-start gap-3">
                <div :class="[notif.color, 'p-2 rounded-full text-white shrink-0 mt-0.5']">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="notif.icon"/></svg>
                </div>
                <div class="flex-1 min-w-0">
                  <p class="text-xs font-semibold text-slate-800 truncate">{{ notif.title }}</p>
                  <p class="text-[11px] text-slate-400 truncate">{{ notif.desc }}</p>
                </div>
                <span class="text-[10px] text-slate-400 shrink-0">{{ notif.time }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- FOOTER -->
        <footer class="flex items-center justify-between pt-4 border-t border-slate-200 text-[11px] text-slate-400">
          <p>© 2025 Distributed ERP. All rights reserved.</p>
          <p>Version 1.0.0</p>
        </footer>
      </main>
    </div>
  </div>
</template>