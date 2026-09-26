import customtkinter as ctk

from app.core.debloat import get_default_debloat_actions
from app.core.focus_manager import FocusManager
from app.core.performance import calculate_performance_score, get_system_metrics


class PCOptimizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PC Performance Optimizer")
        self.geometry("1120x760")
        self.minsize(980, 660)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.focus_manager = FocusManager()
        self.debloat_actions = get_default_debloat_actions()
        self.metrics = get_system_metrics()
        self.score = calculate_performance_score(self.metrics)

        self.configure(fg_color="#0b1020")
        self.build_ui()
        self.update_metrics()

    def build_ui(self):
        self.main_container = ctk.CTkFrame(self, fg_color="#0b1020")
        self.main_container.pack(fill="both", expand=True, padx=22, pady=18)

        self.header = ctk.CTkFrame(self.main_container, corner_radius=18, fg_color="#101827")
        self.header.pack(fill="x", pady=(0, 18))

        self.title_label = ctk.CTkLabel(
            self.header,
            text="Performance + Focus",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#e5eefb",
            padx=24,
            pady=20,
        )
        self.title_label.pack(anchor="w")

        self.dashboard = ctk.CTkFrame(self.main_container, corner_radius=18, fg_color="#101827")
        self.dashboard.pack(fill="x", pady=(0, 18))

        self.score_card = ctk.CTkFrame(self.dashboard, width=300, height=220, corner_radius=20, fg_color="#162238")
        self.score_card.pack(side="left", padx=18, pady=18)
        self.score_card.pack_propagate(False)

        self.score_title = ctk.CTkLabel(self.score_card, text="Performance Score", font=ctk.CTkFont(size=18, weight="bold"), text_color="#dfeafc")
        self.score_title.pack(anchor="w", padx=18, pady=(18, 4))

        self.score_value = ctk.CTkLabel(self.score_card, text="0/100", font=ctk.CTkFont(size=52, weight="bold"), text_color="#6fe7b1")
        self.score_value.pack(anchor="w", padx=18)

        self.score_bar = ctk.CTkProgressBar(self.score_card, width=240, height=12, progress_color="#5eead4")
        self.score_bar.set(0)
        self.score_bar.pack(padx=18, pady=(10, 10))

        self.score_note = ctk.CTkLabel(self.score_card, text="System is running cleanly.", font=ctk.CTkFont(size=13), text_color="#9cc3ff")
        self.score_note.pack(anchor="w", padx=18, pady=(0, 12))

        self.metrics_panel = ctk.CTkFrame(self.dashboard, corner_radius=20, fg_color="#162238")
        self.metrics_panel.pack(side="left", fill="both", expand=True, padx=(0, 18), pady=18)

        self.metrics_label = ctk.CTkLabel(self.metrics_panel, text="Live system health", font=ctk.CTkFont(size=18, weight="bold"), text_color="#dfeafc")
        self.metrics_label.pack(anchor="w", padx=18, pady=(18, 10))

        self.metric_frame = ctk.CTkFrame(self.metrics_panel, fg_color="#101827", corner_radius=16)
        self.metric_frame.pack(fill="x", padx=18, pady=(0, 18))

        self.metric_cpu = self.make_metric_row("CPU", "0%")
        self.metric_ram = self.make_metric_row("RAM", "0%")
        self.metric_disk = self.make_metric_row("Disk", "0%")

        self.action_row = ctk.CTkFrame(self.main_container, fg_color="#101827", corner_radius=18)
        self.action_row.pack(fill="x", pady=(0, 18))

        self.scan_button = ctk.CTkButton(self.action_row, text="Scan system", command=self.scan_system, fg_color="#1d4ed8", hover_color="#1e40af")
        self.scan_button.pack(side="left", padx=18, pady=18)

        self.optimize_button = ctk.CTkButton(self.action_row, text="Optimize now", command=self.optimize_now, fg_color="#0f766e", hover_color="#115e59")
        self.optimize_button.pack(side="left", padx=(0, 18), pady=18)

        self.focus_toggle = ctk.CTkSwitch(self.action_row, text="Focus Mode", command=self.toggle_focus_mode, font=ctk.CTkFont(size=14, weight="bold"), switch_width=52, switch_height=26)
        self.focus_toggle.pack(side="right", padx=18, pady=18)

        self.focus_label = ctk.CTkLabel(self.action_row, text="Focus Mode is off.", font=ctk.CTkFont(size=14), text_color="#b9c9e8")
        self.focus_label.pack(side="right", padx=(0, 14), pady=18)

        self.bottom = ctk.CTkFrame(self.main_container, fg_color="#101827", corner_radius=18)
        self.bottom.pack(fill="both", expand=True)

        self.debloat_panel = ctk.CTkFrame(self.bottom, fg_color="#162238", corner_radius=18)
        self.debloat_panel.pack(side="left", fill="both", expand=True, padx=18, pady=18)

        self.debloat_title = ctk.CTkLabel(self.debloat_panel, text="Debloat checklist", font=ctk.CTkFont(size=22, weight="bold"), text_color="#dfeafc")
        self.debloat_title.pack(anchor="w", padx=18, pady=(18, 12))

        self.debloat_list = []
        for item in self.debloat_actions:
            checkbox = ctk.CTkCheckBox(
                self.debloat_panel,
                text=item.title,
                font=ctk.CTkFont(size=14),
                checkbox_height=18,
                checkbox_width=18,
                onvalue=True,
                offvalue=False,
                fg_color="#60a5fa",
                hover_color="#3b82f6",
            )
            checkbox.pack(anchor="w", padx=18, pady=(0, 12))
            self.debloat_list.append(checkbox)

        self.restore_button = ctk.CTkButton(
            self.bottom,
            text="Restore Changes",
            command=self.restore_changes,
            fg_color="#4b5563",
            hover_color="#374151",
            width=220,
            height=42,
        )
        self.restore_button.pack(anchor="s", padx=18, pady=18)

    def make_metric_row(self, label, value):
        row = ctk.CTkFrame(self.metric_frame, fg_color="#101827")
        row.pack(fill="x", padx=18, pady=(14, 0))

        name = ctk.CTkLabel(row, text=label, font=ctk.CTkFont(size=16), text_color="#dfeafc")
        name.pack(side="left")

        value_label = ctk.CTkLabel(row, text=value, font=ctk.CTkFont(size=16, weight="bold"), text_color="#71e7c8")
        value_label.pack(side="right")

        return value_label

    def update_metrics(self):
        metrics = get_system_metrics()
        self.score = calculate_performance_score(metrics)
        self.score_value.configure(text=f"{self.score}/100")
        self.score_bar.set(self.score / 100)

        self.metric_cpu.configure(text=f"{metrics.cpu}%")
        self.metric_ram.configure(text=f"{metrics.ram}%")
        self.metric_disk.configure(text=f"{metrics.disk}%")

        if self.score >= 80:
            self.score_note.configure(text="System is running cleanly.")
            self.score_value.configure(text_color="#6fe7b1")
        elif self.score >= 60:
            self.score_note.configure(text="A few improvements recommended.")
            self.score_value.configure(text_color="#fbbf24")
        else:
            self.score_note.configure(text="High resource usage detected.")
            self.score_value.configure(text_color="#f87171")

    def scan_system(self):
        self.update_metrics()
        self.focus_label.configure(text="System scan complete.")

    def optimize_now(self):
        self.update_metrics()
        self.score = min(100, self.score + 8)
        self.score_value.configure(text=f"{self.score}/100")
        self.score_bar.set(self.score / 100)
        self.focus_label.configure(text="Optimization plan applied.")

    def toggle_focus_mode(self):
        enabled = self.focus_toggle.get() == 1
        self.focus_manager.toggle(enabled)
        if enabled:
            self.focus_label.configure(text="Focus Mode is active.")
        else:
            self.focus_label.configure(text="Focus Mode is off.")

    def restore_changes(self):
        for checkbox in self.debloat_list:
            checkbox.deselect()
        self.focus_manager.toggle(False)
        self.focus_toggle.deselect()
        self.focus_label.configure(text="Changes restored.")


if __name__ == "__main__":
    app = PCOptimizerApp()
    app.mainloop()
