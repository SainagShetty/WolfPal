class UpdateSchedulesTime < ActiveRecord::Migration[5.1]
  def self.up
    change_table :schedules do |t|
      t.change :time, :string
    end
  end
  def self.down
    change_table :schedules do |t|
      t.change :time, :datetime
    end
  end
end
