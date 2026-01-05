import { Link } from "react-router-dom"

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-neutral-950 text-white">
      <div className="flex">
        {/* Sidebar */}
        <aside className="hidden md:flex md:w-72 md:flex-col md:fixed md:inset-y-0 bg-neutral-900 border-r border-white/10">
          <div className="h-16 flex items-center gap-3 px-6 border-b border-white/10">
            <div className="h-9 w-9 rounded-lg bg-white/10 flex items-center justify-center font-bold">
              ET
            </div>
            <div className="font-semibold">Expense Tracker</div>
          </div>

          <nav className="flex-1 px-4 py-6 space-y-2">
            <SidebarItem to="/dashboard" label="Dashboard" />
            <SidebarItem to="/expenses" label="Expenses" />
            <SidebarItem to="/budgets" label="Budgets" />
            <SidebarItem to="/profile" label="Profile" />
          </nav>

          <div className="px-6 py-4 border-t border-white/10 text-xs text-white/60">
            © 2025 Expense Tracker
          </div>
        </aside>

        {/* Main */}
        <div className="flex-1 md:ml-72">
          {/* Topbar */}
          <header className="h-16 flex items-center justify-between px-6 border-b border-white/10 bg-neutral-900/60 backdrop-blur">
            <div className="font-semibold">Expense Tracker</div>

            <div className="flex items-center gap-4">
              <button className="inline-flex items-center gap-2 rounded-lg border border-white/15 bg-white/5 px-4 py-2 text-sm hover:bg-white/10">
                <span className="text-lg leading-none">+</span>
                Add Expense
              </button>

              <div className="h-9 w-9 rounded-full bg-white/10 flex items-center justify-center text-sm font-semibold">
                AM
              </div>
            </div>
          </header>

          {/* Content */}
          <main className="px-6 py-6">
            {/* Stats row */}
            <div className="grid gap-6 lg:grid-cols-3">
              <StatCard
                title="December Spending"
                value="$2847.32"
                sub="$652.68 remaining of $3500"
                right="↘ 12.5%"
              />
              <StatCard
                title="Budget Status"
                value="81.4%"
                sub="Under budget"
                right=""
              />
              <StatCard
                title="Active Categories"
                value="5"
                sub="Tracking expenses"
                right=""
              />
            </div>

            {/* Charts row */}
            <div className="mt-6 grid gap-6 lg:grid-cols-2">
              <Panel title="Spending by Category">
                <div className="grid gap-6 md:grid-cols-2 items-center">
                  {/* Donut placeholder */}
                  <div className="mx-auto h-56 w-56 rounded-full border border-white/20 bg-white/5" />
                  {/* Legend placeholder */}
                  <div className="space-y-3">
                    {[
                      ["Food & Dining", "$892.50"],
                      ["Transportation", "$420.00"],
                      ["Shopping", "$680.25"],
                      ["Entertainment", "$345.80"],
                      ["Bills", "$508.77"],
                    ].map(([name, amount]) => (
                      <div key={name} className="flex items-center justify-between text-sm">
                        <div className="flex items-center gap-3">
                          <span className="h-2.5 w-2.5 rounded bg-white/40" />
                          <span className="text-white/90">{name}</span>
                        </div>
                        <span className="text-white/70">{amount}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </Panel>

              <Panel title="6-Month Trend">
                {/* Bar chart placeholder */}
                <div className="h-64 rounded-xl border border-white/10 bg-white/5 flex items-end gap-3 p-4">
                  {[70, 82, 76, 92, 86, 84].map((h, i) => (
                    <div key={i} className="flex-1 flex flex-col items-center gap-2">
                      <div
                        className="w-full rounded-lg bg-white/20"
                        style={{ height: `${h}%` }}
                      />
                      <div className="text-xs text-white/60">
                        {["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][i]}
                      </div>
                    </div>
                  ))}
                </div>
              </Panel>
            </div>

            {/* Recent expenses */}
            <div className="mt-6">
              <Panel title="Recent Expenses">
                <div className="-mx-4 mt-2 border-t border-white/10">
                  <div className="divide-y divide-white/10">
                    <ExpenseRow name="Grocery Store" category="Food & Dining" amount="$127.45" date="Dec 18" />
                    <ExpenseRow name="Uber" category="Transportation" amount="$18.50" date="Dec 17" />
                    <ExpenseRow name="Internet Bill" category="Bills" amount="$45.00" date="Dec 16" />
                  </div>
                </div>
              </Panel>
            </div>
          </main>
        </div>
      </div>
    </div>
  )
}

function SidebarItem({ to, label }) {
  return (
    <Link
      to={to}
      className="flex items-center gap-3 rounded-xl px-4 py-3 text-sm text-white/80 hover:bg-white/5 hover:text-white"
    >
      <span className="h-9 w-9 rounded-lg bg-white/10" />
      <span className="font-medium">{label}</span>
    </Link>
  )
}

function StatCard({ title, value, sub, right }) {
  return (
    <div className="rounded-2xl border border-white/15 bg-white/[0.04] p-6">
      <div className="flex items-start justify-between">
        <div className="text-sm text-white/70">{title}</div>
        {right ? <div className="text-sm text-white/70">{right}</div> : null}
      </div>
      <div className="mt-3 text-3xl font-semibold">{value}</div>
      <div className="mt-10 text-sm text-white/70">{sub}</div>
    </div>
  )
}

function Panel({ title, children }) {
  return (
    <div className="rounded-2xl border border-white/15 bg-white/[0.04] p-4">
      <div className="px-2 py-2 text-sm font-semibold text-white/90">
        {title}
      </div>
      <div className="px-2 pb-2">{children}</div>
    </div>
  )
}

function ExpenseRow({ name, category, amount, date }) {
  return (
    <div className="flex items-center justify-between px-4 py-4">
      <div>
        <div className="font-medium">{name}</div>
        <div className="text-sm text-white/60">{category}</div>
      </div>
      <div className="text-right">
        <div className="font-semibold">{amount}</div>
        <div className="text-sm text-white/60">{date}</div>
      </div>
    </div>
  )
}
